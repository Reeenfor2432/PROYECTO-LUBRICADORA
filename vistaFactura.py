import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from claseUtilitaria import claseUtilitaria
from Guardado_de_datos.Conexion import *


class vistaFactura:
    
    def generarFactura(self, base, callbackMenu):
        self.base = base
        self.callbackMenu = callbackMenu
        self.descuento = 1
        self.impuesto = 1
        self.total_final = 0

        self.seleccionCita()
        Button(self.base, text="Volver al menú", command=self.callbackMenu).pack(pady=30)

    def seleccionCita(self):
        self.groupBox = LabelFrame(self.base, text="Selección de la cita a facturar", padx=10, pady=10)
        self.groupBox.pack(pady=50)

        Label(self.groupBox, text="Ingrese ID de la cita:", width=35, font=("arial", 12)).grid(row=0, column=0)
        self.textId = Entry(self.groupBox)
        self.textId.grid(row=0, column=1)

        btnSeleccionar = Button(self.groupBox, text="Seleccionar", width=25, command=self.buscarCliente)
        btnSeleccionar.grid(row=1, column=1)

    def buscarCliente(self):
        self.id_cita = self.textId.get()

        try:
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()

            sql = "SELECT id_cliente FROM cita WHERE id_cita = %s"
            cursor.execute(sql, (self.id_cita,))
            resultado = cursor.fetchone()

            if resultado:
                self.id_cliente = resultado[0]
                self.ingresarDescuento()
            else:
                messagebox.showerror("Error", "La cita no existe.")

            cursor.close()
            conec.close()
        except mysql.connector.Error as error:
            print("Error al conectar: {}".format(error))

    def ingresarDescuento(self):
        # limpiamos el groupBox y mostramos nuevo contenido
        try:
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()

            # Verifica cuántas citas tiene el cliente
            sql = "SELECT COUNT(*) FROM cita WHERE id_cliente = %s"
            cursor.execute(sql, (self.id_cliente,))
            resultado = cursor.fetchone()

            cursor.close()
            conec.close()
        except mysql.connector.Error as error:
            print("Error al conectar: {}".format(error))
            return

        # Limpia la vista (groupBox)
        claseUtilitaria.limpiarGroupbox(self.groupBox)

        if resultado and resultado[0] > 5:
            # El cliente es frecuente entonces mostrar campo para ingresar descuento
            Label(self.groupBox, text="El cliente es frecuente. ¿Desea aplicar un descuento (%)?", width=60).pack(pady=10)
            self.textDescuento = Entry(self.groupBox)
            self.textDescuento.pack(pady=10)

            Button(self.groupBox, text="Aplicar descuento", width=20, command=self.validarDescuento).pack(pady=10)
        else:
            # Cliente no frecuente entonces saltar directo al impuesto
            self.descuento = 1
            self.ingresarImpuesto()

    def validarDescuento(self):
        try:
            descuento = float(self.textDescuento.get())
            if 0 <= descuento <= 100:
                self.descuento = 1 - (descuento / 100)
            else:
                messagebox.showerror("Error", "Descuento inválido")
                return
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido")
            return

        self.ingresarImpuesto()

    def ingresarImpuesto(self):
        # limpiamos y mostramos el ingreso del impuesto
        claseUtilitaria.limpiarGroupbox(self.groupBox)

        Label(self.groupBox, text="Ingrese impuesto o IVA (%):", width=60).pack(pady=10)
        self.textImpuesto = Entry(self.groupBox)
        self.textImpuesto.pack(pady=10)

        btnFinalizar = Button(self.groupBox, text="Generar Factura", command=self.mostrarFactura)
        btnFinalizar.pack(pady=10)

    def mostrarFactura(self):
        try:
            impuesto = float(self.textImpuesto.get())
            if impuesto < 0 or impuesto > 100:
                messagebox.showerror("Error", "IVA inválido")
                return
            self.impuesto = 1 + (impuesto / 100)
        except ValueError:
            messagebox.showerror("Error", "Ingrese un IVA válido")
            return

        # Consulta del subtotal
        try:
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()

            sql_subtotal = """
                SELECT SUM(s.precio) AS subtotal
                FROM Detalle_Servicio ds
                JOIN servicio s using (id_servicio)
                WHERE ds.id_cita = %s
            """
            cursor.execute(sql_subtotal, (self.id_cita,))  # Usamos el id_cita ingresado
            resultado = cursor.fetchone()
            cursor.close()
            conec.close()

            if resultado and resultado[0] is not None:
                self.subtotal = float(resultado[0])
            else:
                messagebox.showerror("Error", "No hay servicios registrados para esta cita.")
                return
            
            # Consulta detallada de servicios
            sql_servicios = """
                SELECT s.nombre, COUNT(ds.id_servicio) AS cantidad,
                       s.precio, COUNT(ds.id_servicio) * s.precio AS total
                FROM Detalle_Servicio ds
                JOIN servicio s ON ds.id_servicio = s.id_servicio
                WHERE ds.id_cita = %s
                GROUP BY s.id_servicio, s.nombre, s.precio
            """
            cursor.execute(sql_servicios, (self.id_cita,))
            self.servicios = cursor.fetchall()

        except mysql.connector.Error as error:
            print("Error al conectar: {}".format(error))
            return
        

        #Calculos
        total_con_descuento = self.subtotal * self.descuento
        self.total_final = total_con_descuento * self.impuesto

        # limpiamos y mostramos factura
        claseUtilitaria.limpiarVentana(self.base)
        facturaBox = LabelFrame(self.base, text="Factura generada", padx=10, pady=10)
        facturaBox.pack(pady=50)

        self.cedula= claseUtilitaria.buscarCedulaPorId(self.id_cliente)

        Label(facturaBox, text=f"Cedula del Cliente: {self.cedula}", font=("arial", 18)).pack()
        Label(facturaBox, text=f"Subtotal: ${self.subtotal:.2f}", font=("arial", 14)).pack()
        Label(facturaBox, text=f"Descuento aplicado: {(1 - self.descuento) * 100:.0f}%", font=("arial", 14)).pack()
        Label(facturaBox, text=f"IVA aplicado: {(self.impuesto - 1) * 100:.0f}%", font=("arial", 14)).pack()
        Label(facturaBox, text=f"Total a pagar: ${self.total_final:.2f}", font=("arial", 22, "bold")).pack(pady=10)
        
        Button(self.base, text="Volver al menú", command=self.callbackMenu).pack(pady=30)
        
        #Tabla de servicios
        tablaBox = LabelFrame(facturaBox, text="Servicios usados", padx=10, pady=10)
        tablaBox.pack(pady=10)

        tabla = ttk.Treeview(tablaBox, columns=("Servicio", "Cantidad", "Precio", "Total"), show="headings")
        tabla.heading("Servicio", text="Servicio")
        tabla.heading("Cantidad", text="Cantidad")
        tabla.heading("Precio", text="Precio Unitario")
        tabla.heading("Total", text="Total")

        tabla.column("Servicio", width=150)
        tabla.column("Cantidad", width=80, anchor="center")
        tabla.column("Precio", width=120, anchor="e")
        tabla.column("Total", width=120, anchor="e")

        tabla.pack()

        for serv in self.servicios:
            tabla.insert("", "end", values=(serv[0], serv[1], f"${serv[2]:.2f}", f"${serv[3]:.2f}"))

        Button(self.base, text="Volver al menú", command=self.callbackMenu).pack(pady=30)
    
    def guaradarFactura(self):
        try:
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()
            cursor.callproc("sp_insertar_factura", (self.id_cita, self.subtotal, self.total_final, self.impuesto, self.descuento))
            conec.commit()
            cursor.close()
            conec.close()
            messagebox.showinfo("Éxito", "Factura guardada correctamente.")
        except mysql.connector.Error as error:
            print("Error al insertar factura: {}".format(error))
            messagebox.showerror("Error", "No se pudo guardar la factura.")
