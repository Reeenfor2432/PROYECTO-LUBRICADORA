import mysql.connector
from Guardado_de_datos.Conexion import CConexion

class manejarServicio:

    def MostrarServicios():
        try:
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor(dictionary=True)
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
            return True, "Servicio agregado correctamente"
        except mysql.connector.Error as error:
            print("Error al insertar servicio: {}".format(error))

    def ModificarServicio(id, nombre, descripcion, precio):
        try:
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()
            cursor.callproc("sp_actualizar_servicio", (int(id), nombre, descripcion, precio))
            conec.commit(); conec.close()
            return True, "Servicio modificado correctamente"
        except mysql.connector.Error as error:
            print("Error al actualizar servicio: {}".format(error))

    def EliminarServicio(id):
        try:
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()
            cursor.callproc("sp_eliminar_servicio", (int(id),))
            conec.commit(); conec.close()
            return True, "Servicio eliminado correctamente"
        except mysql.connector.Error as error:
            print("Error al eliminar servicio: {}".format(error))