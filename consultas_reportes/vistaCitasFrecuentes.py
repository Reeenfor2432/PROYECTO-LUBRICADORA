import tkinter as tk
from tkinter import *
from tkinter import ttk
from claseUtilitaria import claseUtilitaria
from Guardado_de_datos.Conexion import *

class vistaCitasFrecuentes:
        def interfazCitasFrecuentes(self,tabla):
            self.tabla= tabla
            self.actualizarVistaTabla()
        
        def actualizarVistaTabla(self):
            try:
                self.tabla.delete(*self.tabla.get_children())  # limpiar tabla

                datos = self.MostrarCitasFrecuentes()
                for row in datos:
                    self.tabla.insert("", "end", values=row)

            except Exception as error:
                print("Error al actualizar tabla: {}".format(error))
    
        def MostrarCitasFrecuentes(self):
            try:
                conec = CConexion.ConexionBaseDeDatos()
                cursor = conec.cursor()
                cursor.execute("SELECT c.id_cita, c.id_cliente, c.placa, c.id_empleado, c.hora_ingreso, c.hora_salida, c.estado FROM cita c JOIN cliente cl ON c.id_cliente = cl.id_cliente WHERE c.id_cliente IN (SELECT id_cliente FROM cita GROUP BY id_cliente HAVING COUNT(*) > 5);")
                resultado = cursor.fetchall()
                conec.close()
                return resultado
            
            except mysql.connector.Error as error:
                print("Error al intentar mostrar los datos {}".format(error))
            finally:
                conec.close()