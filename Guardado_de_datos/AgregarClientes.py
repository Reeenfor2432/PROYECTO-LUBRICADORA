from .Conexion import *

class Aggclientes:
    def MostrarClientes():
        try:
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()
            cursor.execute("SELECT cedula,nombre_cliente,telefono FROM cliente;")
            resultado = cursor.fetchall()
            conec.close()
            return resultado
        
        except mysql.connector.Error as error:
            print("Error al intentar mostrar los datos {}".format(error))
        finally:
            conec.close()



    def IngresarClientes(cedula,nombre,telefono):
        try:
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()

            sql ="insert into cliente values(null,%s,%s,%s);"
            valores = (cedula,nombre,telefono)
            cursor.execute(sql,valores)
            conec.commit()
            print(cursor.rowcount,"Registro ingresado con exito")
        except mysql.connector.Error as error:
            print("Error al intentar ingresar los datos {}".format(error))
        finally:
            conec.close()


