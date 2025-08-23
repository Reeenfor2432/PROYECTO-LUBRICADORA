from Guardado_de_datos.AdminCitas import manejarCita
from tkinter import *
from tkinter import messagebox, ttk
import tkinter as tk
from claseUtilitaria import claseUtilitaria
from Guardado_de_datos.Conexion import *
from Guardado_de_datos.db import conn, cursor

class vistaCita:

    def generarCita(self, base, callbackMenu):
        self.base = base
        self.callbackMenu = callbackMenu

        groupBoxdatos = LabelFrame(base, text="Datos de la Cita", padx=10, pady=10)
        groupBoxdatos.pack(pady=20)

        Label(groupBoxdatos, text="ID Cita:", width=25).grid(row=0, column=0)
        self.textId = Entry(groupBoxdatos); self.textId.grid(row=0, column=1)

        Label(groupBoxdatos, text="ID Cliente:", width=25).grid(row=1, column=0)
        self.textNom = Entry(groupBoxdatos); self.textNom.grid(row=1, column=1)

        Label(groupBoxdatos, text="Placa:", width=25).grid(row=2, column=0)
        self.textP = Entry(groupBoxdatos); self.textP.grid(row=2, column=1)

        Label(groupBoxdatos, text="ID Empleado:", width=25).grid(row=3, column=0)
        self.textEmp = Entry(groupBoxdatos); self.textEmp.grid(row=3, column=1)

        Label(groupBoxdatos, text="Hora ingreso:", width=25).grid(row=4, column=0)
        self.texting = Entry(groupBoxdatos); self.texting.grid(row=4, column=1)

        Label(groupBoxdatos, text="Hora salida:", width=25).grid(row=5, column=0)
        self.textsal = Entry(groupBoxdatos); self.textsal.grid(row=5, column=1)

        Label(groupBoxdatos, text="Estado:", width=25).grid(row=6, column=0)
        self.textEst = Entry(groupBoxdatos); self.textEst.grid(row=6, column=1)

        # botones
        Button(groupBoxdatos, text="Generar", width=12, command=self.guardar).grid(row=7, column=0)
        Button(groupBoxdatos, text="Modificar", width=12, command=self.modificar).grid(row=7, column=1)
        Button(groupBoxdatos, text="Eliminar", width=12, command=self.eliminar).grid(row=7, column=2)

        if callbackMenu:
            Button(base, text="Volver al menú", command=callbackMenu).pack(pady=10)

        #Tabla para cita estándar
        groupBoxTabla = LabelFrame(base, text="Lista de Citas", padx=10, pady=10)
        groupBoxTabla.pack(pady=20)
        self.tabla= ttk.Treeview(groupBoxTabla, columns=("id_cita","cedula","placa","id_empleado","hora_ingreso","hora_salida","estado"),show="headings")
        self.tabla.heading("id_cita", text="Identificacion")
        self.tabla.column("id_cita",width=100, anchor="w")
        self.tabla.heading("cedula", text= "Identificación del cliente")
        self.tabla.column("cedula",width=120, anchor="w")
        self.tabla.heading("placa", text= "Placa del vehículo")
        self.tabla.column("placa",width=120, anchor="w")
        self.tabla.heading("id_empleado", text="ID del empleado")
        self.tabla.column("id_empleado",width=120, anchor="w")
        self.tabla.heading("hora_ingreso", text= "Hora de ingreso")
        self.tabla.column("hora_ingreso",width=120, anchor="w")
        self.tabla.heading("hora_salida", text= "Hora de salida")
        self.tabla.column("hora_salida",width=120, anchor="w")
        self.tabla.heading("estado", text= "Estado de la cita")
        self.tabla.column("estado",width=100, anchor="w")
        self.tabla.pack()

        self.tabla.bind("<<TreeviewSelect>>", self.seleccionarRegistro)
        self.actualizarVistaTabla()

    def guardar(self):
        id_cita = manejarCita.IngresarCita(
            self.textNom.get(), self.textP.get(), self.textEmp.get(),
            self.texting.get(), self.textsal.get(), self.textEst.get())
        
        if id_cita:
            self.id_cita_generada = id_cita
            messagebox.showinfo("OK", "Cita generada.")
            self.actualizarVistaTabla()

            self.asignarProducto()

    def modificar(self):
        manejarCita.ModificarCita(self.textId.get(),self.textNom.get(), self.textP.get(), self.textEmp.get(),
            self.texting.get(), self.textsal.get(), self.textEst.get())
        messagebox.showinfo("OK", "Cita modificada.")
        self.actualizarVistaTabla()

    def eliminar(self):
        self.eliminarProductoUsado()
        manejarCita.EliminarCita(self.textId.get())
        messagebox.showinfo("OK", "Cita eliminada.")
        self.actualizarVistaTabla()
        

    def actualizarVistaTabla(self):
        self.tabla.delete(*self.tabla.get_children())
        for row in manejarCita.MostrarCita():
            self.tabla.insert("", "end", values=(row["id_cita"], row["id_cliente"], row["placa"], 
                                                 row["id_empleado"], row["hora_ingreso"], row["hora_salida"], row["estado"]))

    def seleccionarRegistro(self, _):
        vals = self.tabla.item(self.tabla.focus())["values"]
        if vals:
            self.textId.delete(0, END); self.textId.insert(0, vals[0])
            self.textNom.delete(0, END); self.textNom.insert(0, vals[1])
            self.textP.delete(0, END); self.textP.insert(0, vals[2])
            self.textEmp.delete(0, END); self.textEmp.insert(0, vals[3])
            self.texting.delete(0, END); self.texting.insert(0, vals[4])
            self.textsal.delete(0, END); self.textsal.insert(0, vals[5])
            self.textEst.delete(0, END); self.textEst.insert(0, vals[6])
    
    # INSERTS PARA PRODUCTO USADO 
    def asignarProducto(self): 
        claseUtilitaria.limpiarVentana(self.base) 
        groupBoxProd= LabelFrame(self.base, text= "Asignación de Productos", padx=10, pady=10) 
        groupBoxProd.pack(pady=50) 
        self.LabelProd= Label(groupBoxProd, text= "Ingrese el producto a usar en la cita:", width=35, font=("arial",20)) 
        self.LabelProd.grid(row=0, column=0) 
        self.textProd = tk.Entry(groupBoxProd) 
        self.textProd.grid(row=0,column=1) 
        self.LabelPCant= Label(groupBoxProd, text= "Cantidad a usar:", width=35, font=("arial",20)) 
        self.LabelPCant.grid(row=1, column=0) 
        self.textPCant = tk.Entry(groupBoxProd) 
        self.textPCant.grid(row=1,column=1) 
        Button(groupBoxProd, text="Añadir", width=15, command=self.insertarProductoUsado).grid(row=7, column=0) 
        
    def insertarProductoUsado(self): 
        try:
            sql = """INSERT INTO producto_usado (id_cita, id_producto, cantidad) VALUES (%s,%s,%s)""" 
            datos = (self.id_cita_generada, self.textProd.get(), self.textPCant.get()) 
            cursor.execute(sql, datos) 
            conn.commit() 
            messagebox.showinfo("OK","Se han asignado los productos a la cita") 
            claseUtilitaria.limpiarVentana(self.base) 
            self.generarCita(self.base, self.callbackMenu)
        except mysql.connector.Error as error:
            print("Error al intentar asignar los productos {}".format(error))
    
    def eliminarProductoUsado(self): 
        try:
            sql = """DELETE FROM producto_usado WHERE id_cita = %s""" 
            datos = (self.textId.get(),) 
            cursor.execute(sql, datos) 
            conn.commit()
            print("Se han retirado los productos de la cita") 
        except mysql.connector.Error as error:
            print("Error al intentar remover los productos {}".format(error))



