import tkinter as tk
from tkinter import *
from tkinter import ttk
from Guardado_de_datos.Conexion import *
from claseUtilitaria import claseUtilitaria

class vistaReporteFactura:
    def interfazReporteFactura(self,base):
        groupBox = LabelFrame(base, text="Lista de Facturas", padx=5, pady=5)
        groupBox.pack(pady=10)

        # Creación del TreeView (igual que tu formato)
        self.tabla = ttk.Treeview(
        groupBox,
        columns=("id_factura", "subtotal", "impuesto", "descuento", "total","id_cita", "nombre_cliente", "cedula", "placa"),show="headings",height=5,)

    # Encabezados de las columnas
        self.tabla.heading("id_factura", text="ID Factura")
        self.tabla.heading("subtotal", text="Subtotal")
        self.tabla.heading("impuesto", text="Impuesto")
        self.tabla.heading("descuento", text="Descuento")
        self.tabla.heading("total", text="Total")
        self.tabla.heading("id_cita", text="ID Cita")
        self.tabla.heading("nombre_cliente", text="Cliente")
        self.tabla.heading("cedula", text="Cédula")
        self.tabla.heading("placa", text="Placa Vehículo")

        self.tabla.column("id_factura", anchor="w")
        self.tabla.column("subtotal", anchor="w")
        self.tabla.column("impuesto", anchor="w")
        self.tabla.column("descuento", anchor="w")
        self.tabla.column("total", anchor="w")
        self.tabla.column("id_cita", anchor="w")
        self.tabla.column("nombre_cliente", anchor="w")
        self.tabla.column("cedula", anchor="w")
        self.tabla.column("placa", anchor="w")

        self.tabla.pack(pady=10)

    # Llamada al método que actualiza la tabla
        self.actualizarVistaTabla()
        return groupBox
    
    def actualizarVistaTabla(self):
        try:
            self.tabla.delete(*self.tabla.get_children())  # limpiar tabla

            datos = self.MostrarReporteFactura()
            for row in datos:
                self.tabla.insert("", "end", values=row)

        except Exception as error:
            print("Error al actualizar tabla: {}".format(error))
    
    def MostrarReporteFactura(self):
        try:
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()
            cursor.execute("SELECT * FROM facturaDetallada")
            resultado = cursor.fetchall()
            conec.close()
            return resultado
        
        except mysql.connector.Error as error:
            print("Error al intentar mostrar los datos {}".format(error))
        finally:
            conec.close()
