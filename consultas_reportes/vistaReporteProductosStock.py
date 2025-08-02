import tkinter as tk
from tkinter import *
from tkinter import ttk
from Guardado_de_datos.Conexion import *
from claseUtilitaria import claseUtilitaria

class vistaReporteProductosStock:
    def interfazReporteStock(self,base):
        groupBox= LabelFrame(base,text="Lista de Productos", padx=5,pady=5,)
        groupBox.pack(pady=10)
        #Crecion de TreeView (widget que permite mostrar tablas)
        self.tabla= ttk.Treeview(groupBox,columns=("id_producto","nombre_producto","descripcion", "precio_unitario", "stock", "id_marca", "id_categoria"), show="headings", height=5,)
        self.tabla.heading("id_producto", text="Identificacion")
        self.tabla.column("id_producto",width=100, anchor="w")
        self.tabla.heading("nombre_producto", text= "Nombre del producto")
        self.tabla.column("nombre_producto",width=130, anchor="w")
        self.tabla.heading("descripcion", text= "Descripcion")
        self.tabla.column("descripcion",width=300, anchor="w")
        self.tabla.heading("precio_unitario", text= "Precio unitario")
        self.tabla.column("precio_unitario",width=90, anchor="w")
        self.tabla.heading("stock", text= "Stock actual")
        self.tabla.column("stock",width=90, anchor="w")
        self.tabla.heading("id_marca", text= "ID Marca")
        self.tabla.column("id_marca",width=90, anchor="w")
        self.tabla.heading("id_categoria", text= "ID Categoría")
        self.tabla.column("id_categoria",width=90, anchor="w")
        self.tabla.pack(pady=10)
        self.actualizarVistaTabla()
        return groupBox

    def actualizarVistaTabla(self):
        try:
            self.tabla.delete(*self.tabla.get_children())  # limpiar tabla

            datos = self.MostrarReporteStock()
            for row in datos:
                self.tabla.insert("", "end", values=row)

        except Exception as error:
            print("Error al actualizar tabla: {}".format(error))
    
    def MostrarReporteStock(self):
        try:
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()
            cursor.execute("SELECT id_producto,nombre_producto,descripcion, precio_unitario, stock, id_marca, id_categoria FROM producto WHERE stock < 5")
            resultado = cursor.fetchall()
            conec.close()
            return resultado
        
        except mysql.connector.Error as error:
            print("Error al intentar mostrar los datos {}".format(error))
        finally:
            conec.close()

 