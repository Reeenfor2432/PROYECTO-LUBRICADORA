from .Conexion import *  # Importa la conexión a la base de datos desde el módulo Conexion

class manejarCliente:
    
    # Método para mostrar todos los clientes en la base de datos
    def MostrarClientes():
        try:
            # Crear una conexión con la base de datos
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()  # Crear un cursor para ejecutar consultas
            cursor.execute("SELECT * FROM cliente;")  # Ejecutar la consulta para seleccionar todos los registros de clientes
            resultado = cursor.fetchall()  # Obtener todos los registros resultantes
            conec.commit()  # Confirmar la transacción
            conec.close()  # Cerrar la conexión a la base de datos
            return resultado  # Retornar los resultados obtenidos

        except mysql.connector.Error as error:
            print("Error al intentar mostrar los datos {}".format(error))  # En caso de error, se muestra el mensaje

    # Método para insertar un nuevo cliente en la base de datos
    def IngresarClientes(cedula, nombre, telefono):
        try:
            # Crear una conexión con la base de datos
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()
            # SP que realiza el SQL con procedure
            cursor.callproc("sp_insertar_cliente", (cedula, nombre, telefono))
            conec.commit()
            print("Registro ingresado con éxtio")
            conec.close()
        except mysql.connector.Error as error:
            print("Error al intentar ingresar los datos {}".format(error))  # En caso de error, se muestra el mensaje


    # Método para modificar un cliente existente en la base de datos
    def ModificarClientes(id, cedula, nombre, telefono):
        try:
            # Crear una conexión con la base de datos
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()
            # SP que realiza el SQL con procedure
            cursor.callproc("sp_actualizar_cliente", (int(id), cedula, nombre, telefono))
            conec.commit()
            print("Registro actualizado con éxtio")
            conec.close()
        except mysql.connector.Error as error:
            print("Error al intentar ingresar los datos {}".format(error))  # En caso de error, se muestra el mensaje

    # Método para eliminar un cliente de la base de datos
    def EliminarClientes(id):
        try:
            # Crear una conexión con la base de datos
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()
            # SP que realiza el SQL con procedure
            cursor.callproc("sp_eliminar_cliente", (int(id),))
            conec.commit()
            print("Registro eliminado con éxtio")
            conec.close()
        except mysql.connector.Error as error:
            print("Error al intentar ingresar los datos {}".format(error))  # En caso de error, se muestra el mensaje