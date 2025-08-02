import tkinter as tk
from tkinter import *
from tkinter import ttk
from Guardado_de_datos.Conexion import *
from claseUtilitaria import claseUtilitaria

class vistaReporteIngreso:
    def interfazReporteIngreso(self,base):
        groupBox= LabelFrame(base,text="Lista de Citas", padx=5,pady=5,)
        groupBox.pack(pady=10)
        #Crecion de TreeView (widget que permite mostrar tablas)
        self.tabla= ttk.Treeview(groupBox,columns=("id_cita","totalIngresoServicio"), show="headings", height=5,)
        self.tabla.heading("id_cita", text="Identificacion de la cita")
        self.tabla.heading("totalIngresoServicio", text= "Total ingresado por servicio")

        self.tabla.pack(pady=10)
        self.actualizarVistaTabla()
        return groupBox

    def actualizarVistaTabla(self):
        try:
            self.tabla.delete(*self.tabla.get_children())  # limpiar tabla

            datos = self.MostrarReporteIngreso()
            for row in datos:
                self.tabla.insert("", "end", values=row)

        except Exception as error:
            print("Error al actualizar tabla: {}".format(error))
    
    def MostrarReporteIngreso(self):
        try:
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()
            cursor.execute("SELECT id_cita, subtotal as totalPorServicio FROM cita join factura on id_cita=cita")
            resultado = cursor.fetchall()
            conec.close()
            return resultado
        
        except mysql.connector.Error as error:
            print("Error al intentar mostrar los datos {}".format(error))
        finally:
            conec.close()
