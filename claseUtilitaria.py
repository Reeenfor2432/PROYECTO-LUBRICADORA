import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from Guardado_de_datos.Conexion import *

#Métodos utilitarios
class claseUtilitaria:
    @staticmethod
    def limpiarVentana(base):
        for elemento in base.winfo_children():
            elemento.destroy()
    @staticmethod
    def limpiarTabla(tabla):
        for fila in tabla.get_children():
            tabla.delete(fila)

    @staticmethod
    def tablaParaCita(base):
        groupbox= LabelFrame(base, text="Lista de Citas", padx=5, pady=5,)
        groupbox.pack(pady=10)

        tabla= ttk.Treeview(groupbox, columns=("id_cita","cedula","placa","id_empleado","hora_ingreso","hora_salida","estado"),show="headings")
        tabla.heading("id_cita", text="Identificacion")
        tabla.column("id_cita",width=100, anchor="w")
        tabla.heading("cedula", text= "Cedula del cliente")
        tabla.column("cedula",width=120, anchor="w")
        tabla.heading("placa", text= "Placa del vehículo")
        tabla.column("placa",width=120, anchor="w")
        tabla.heading("id_empleado", text="ID del empleado")
        tabla.column("id_empleado",width=120, anchor="w")
        tabla.heading("hora_ingreso", text= "Hora de ingreso")
        tabla.column("hora_ingreso",width=120, anchor="w")
        tabla.heading("hora_salida", text= "Hora de salida")
        tabla.column("hora_salida",width=120, anchor="w")
        tabla.heading("estado", text= "Estado de la cita")
        tabla.column("estado",width=100, anchor="w")
        tabla.pack()
        return tabla
    
    @staticmethod
    def eliminarTabla(tabla):
        if tabla is not None:
            tabla.destroy()
    
    @staticmethod
    def limpiarGroupbox(groupB):
        for widget in groupB.winfo_children():
                widget.destroy()
    
    @staticmethod
    def eliminarGroupbox(groupbox):
        if groupbox is not None:
            groupbox.destroy()

    
    #METODOS PARA SQL
    @staticmethod
    def buscarCedulaPorId(id_cliente):
        try:
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()

            sql = "SELECT cedula FROM cliente WHERE id_cliente = %s"
            cursor.execute(sql, (id_cliente,))
            resultado = cursor.fetchone()

            cursor.close()
            conec.close()

            if resultado:
                return resultado[0]  # regresa cedula
            else:
                print("Cliente no encontrado.")
                return None

        except mysql.connector.Error as error:
            print("Error al obtener la cédula del cliente:", error)
            return None