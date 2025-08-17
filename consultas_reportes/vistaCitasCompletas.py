import tkinter as tk
from tkinter import *
from tkinter import ttk
from claseUtilitaria import claseUtilitaria
from Guardado_de_datos.Conexion import *

class vistaCitasCompletas:
        def interfazCitasCompletas(self,tabla):
            self.tabla= tabla
            self.actualizarVistaTabla()
        
        def actualizarVistaTabla(self):
            try:
                self.tabla.delete(*self.tabla.get_children())  # limpiar tabla

                datos = self.MostrarCitasCompletas()
                for row in datos:
                    self.tabla.insert("", "end", values=row)

            except Exception as error:
                print("Error al actualizar tabla: {}".format(error))
    
        def MostrarCitasCompletas(self):
            try:
                conec = CConexion.ConexionBaseDeDatos()
                cursor = conec.cursor()
                cursor.execute("SELECT * FROM citasTodas;")
                resultado = cursor.fetchall()
                conec.close()
                return resultado
            
            except mysql.connector.Error as error:
                print("Error al intentar mostrar los datos {}".format(error))
            finally:
                conec.close()

            
