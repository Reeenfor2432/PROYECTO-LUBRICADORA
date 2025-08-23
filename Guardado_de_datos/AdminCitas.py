from .Conexion import *  # Importa la conexión a la base de datos desde el módulo Conexion

class manejarCita:
    
    def MostrarCita():
        try:
            # Crear una conexión con la base de datos
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()  # Crear un cursor para ejecutar consultas
            cursor.execute("SELECT * FROM cita;")  # Ejecutar la consulta para seleccionar todos los registros de citas
            resultado = cursor.fetchall()  # Obtener todos los registros resultantes
            conec.commit()  # Confirmar la transacción
            conec.close()  # Cerrar la conexión a la base de datos
            return resultado  # Retornar los resultados obtenidos

        except mysql.connector.Error as error:
            print("Error al intentar mostrar los datos {}".format(error))  # En caso de error, se muestra el mensaje

    # Método para insertar bueva cita en la base de datos
    def IngresarCita(id_cliente, placa, id_empleado, hora_ingreso,hora_salida, estado):
        try:
            # Crear una conexión con la base de datos
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()  # Crear un cursor para ejecutar consultas

            # SQL para insertar nueva cita
            cursor.callproc("sp_insertar_cita", (id_cliente, placa, id_empleado, hora_ingreso,hora_salida, estado))
            conec.commit()  # Valores a insertar
            print(cursor.rowcount, "Registro ingresado con exito")  # Informar si el registro fue exitoso
            conec.close()  # Cerrar la conexión a la base de datos

        except mysql.connector.Error as error:
            print("Error al intentar ingresar los datos {}".format(error))  # En caso de error, se muestra el mensaje

    # Método para modificar una cita existente en la base de datos
    def ModificarCita(id_cita, id_cliente, placa, id_empleado, hora_ingreso,hora_salida, estado):
        try:
            # Crear una conexión con la base de datos
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()  # Crear un cursor para ejecutar consultas

            # SQL para actualizar los datos de un empleado
            cursor.callproc("sp_actualizar_cita", (id_cita, id_cliente, placa, id_empleado, hora_ingreso,hora_salida, estado))
            conec.commit()  # Valores a insertar 
            print(cursor.rowcount, "Registro modificado con exito")  # Informar si el registro fue modificado exitosamente
            conec.close()  # Cerrar la conexión a la base de datos

        except mysql.connector.Error as error:
            print("Error al intentar modificar los datos {}".format(error))  # En caso de error, se muestra el mensaje

    # Método para eliminar una cita de la base de datos
    def EliminarCita(id_cita):
        try:
            # Crear una conexión con la base de datos
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()  # Crear un cursor para ejecutar consultas

            # SQL para eliminar un vehiculo por su ID
            cursor.callproc("sp_eliminar_cita", (id_cita))
            conec.commit()  # Valores a insertar 
            print(cursor.rowcount, "Registro eliminado con exito")  # Informar si el registro fue eliminado exitosamente
            conec.close()  # Cerrar la conexión a la base de datos

        except mysql.connector.Error as error:
            print("Error al intentar eliminar los datos {}".format(error))  # En caso de error, se muestra el mensaje
        
    

    @staticmethod
    def obtenerId_cliente(cedula):
        # Crear una conexión con la base de datos
        try:
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()  # Crear un cursor para ejecutar consultas
            sql = "SELECT id_cliente FROM cliente WHERE cedula = %s"
            cursor.execute(sql, (cedula,))
            resultado = cursor.fetchone()

            # Verificar si se encontró una marca
            if resultado:
                id_cliente = resultado[0]  # Devuelve el id
            else:
                print(cursor.rowcount, "La cédula del cliente no existe")
            cursor.close()
            conec.close()
            return id_cliente

        except mysql.connector.Error as error:
            print("Error al conectar {}".format(error))
    