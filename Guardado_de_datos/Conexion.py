import mysql.connector

class CConexion:

    def ConexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(user='root',password='LdJGcoDfHWxFQjGunBXIlrVNbQEEVGcI',
                                               host='gondola.proxy.rlwy.net',database='LUBRICONTROL',
                                               port='35671')
            print("La conexion ha sido exitosa!")
            return conexion

        except mysql.connector.Error as error:
            print("Error al conectarte a la base de datos {}".format(error))
            return conexion
        
    ConexionBaseDeDatos()