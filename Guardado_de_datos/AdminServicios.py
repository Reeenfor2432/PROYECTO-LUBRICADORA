import mysql.connector
from Conexion import CConexion

class manejarServicio:

    def MostrarServicios():
        try:
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()
            cursor.execute("SELECT * FROM servicio;")
            resultado = cursor.fetchall()
            conec.commit(); conec.close()
            return resultado
        except mysql.connector.Error as error:
            print("Error al mostrar servicios: {}".format(error))

    def IngresarServicio(nombre, descripcion, precio):
        try:
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()
            cursor.callproc("sp_insertar_servicio", (nombre, descripcion, precio))
            conec.commit(); conec.close()
            print("Servicio ingresado con éxito")
        except mysql.connector.Error as error:
            print("Error al insertar servicio: {}".format(error))

    def ModificarServicio(id, nombre, descripcion, precio):
        try:
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()
            cursor.callproc("sp_actualizar_servicio", (id, nombre, descripcion, precio))
            conec.commit(); conec.close()
            print("Servicio actualizado con éxito")
        except mysql.connector.Error as error:
            print("Error al actualizar servicio: {}".format(error))

    def EliminarServicio(id):
        try:
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()
            cursor.callproc("sp_eliminar_servicio", (id,))
            conec.commit(); conec.close()
            print("Servicio eliminado con éxito")
        except mysql.connector.Error as error:
            print("Error al eliminar servicio: {}".format(error))