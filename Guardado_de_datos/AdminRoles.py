import mysql.connector
from Guardado_de_datos.Conexion import CConexion

class manejarRol:

    def MostrarRoles():
        try:
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()
            cursor.execute("SELECT * FROM rol;")
            resultado = cursor.fetchall()
            conec.commit(); conec.close()
            return resultado
        except mysql.connector.Error as error:
            print("Error al mostrar roles: {}".format(error))

    def IngresarRol(nombre, descripcion):
        try:
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()
            cursor.callproc("sp_insertar_rol", (nombre, descripcion))
            conec.commit(); conec.close()
            print("Rol ingresado con éxito")
        except mysql.connector.Error as error:
            print("Error al insertar rol: {}".format(error))

    def ModificarRol(id, nombre, descripcion):
        try:
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()
            cursor.callproc("sp_actualizar_rol", (int(id), nombre, descripcion))
            conec.commit(); conec.close()
            print("Rol actualizado con éxito")
        except mysql.connector.Error as error:
            print("Error al actualizar rol: {}".format(error))

    def EliminarRol(id):
        try:
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()
            cursor.callproc("sp_eliminar_rol", (int(id),))
            conec.commit(); conec.close()
            print("Rol eliminado con éxito")
        except mysql.connector.Error as error:
            print("Error al eliminar rol: {}".format(error))
