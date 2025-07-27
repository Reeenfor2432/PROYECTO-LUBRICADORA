from .Conexion import *

class Aggclientes:
    def MostrarClientes():
        try:
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()
            cursor.execute("SELECT * FROM cliente;")
            resultado = cursor.fetchall()
            conec.commit()
            conec.close()
            return resultado
        
        except mysql.connector.Error as error:
            print("Error al intentar mostrar los datos {}".format(error))



    def IngresarClientes(cedula,nombre,telefono):
        try:
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()

            sql ="insert into cliente values(null,%s,%s,%s);"
            valores = (cedula,nombre,telefono)
            cursor.execute(sql,valores)
            conec.commit()
            print(cursor.rowcount,"Registro ingresado con exito")
            conec.close()

        except mysql.connector.Error as error:
            print("Error al intentar ingresar los datos {}".format(error))

    def ModificarClientes(id,cedula,nombre,telefono):
        try:
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()

            sql = "UPDATE cliente SET cedula=%s,nombre_cliente=%s, telefono=%s WHERE id_cliente=%s;"
            valores = (cedula, nombre, telefono, id)
            cursor.execute(sql, valores)
            conec.commit()
            print(cursor.rowcount, "Registro modificado con exito")
            conec.close()

        except mysql.connector.Error as error:
            print("Error al intentar modificar los datos {}".format(error))

    def EliminarClientes(id):
        try:
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()
            sql = "DELETE FROM cliente WHERE id_cliente=%s;"
            valores = (id,)
            cursor.execute(sql, valores)
            conec.commit()
            print(cursor.rowcount, "Registro eliminado con exito")
            conec.close()

        except mysql.connector.Error as error:
            print("Error al intentar eliminar los datos {}".format(error))



