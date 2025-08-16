import mysql.connector  # Importa el conector de MySQL para Python

class CConexion:

    # Método para establecer una conexión a la base de datos
    def ConexionBaseDeDatos():
        try:
            # Intentar establecer una conexión a la base de datos con los parámetros proporcionados
            conexion = mysql.connector.connect(
                user='root',  # Usuario para la base de datos
                password='LdJGcoDfHWxFQjGunBXIlrVNbQEEVGcI',  # Contraseña del usuario
                host='gondola.proxy.rlwy.net',  # Dirección del host de la base de datos
                database='LUBRICONTROL',  # Nombre de la base de datos
                port='35671'  # Puerto de la base de datos
            )
            print("La conexion ha sido exitosa!")  # Si la conexión es exitosa, se imprime un mensaje
            return conexion  # Retorna la conexión establecida

        except mysql.connector.Error as error:
            # Si hay un error en la conexión, se captura y se muestra el mensaje de error
            print("Error al conectarte a la base de datos {}".format(error))
            return conexion  # Retorna la conexión (aunque en caso de error no se ha creado correctamente)
        