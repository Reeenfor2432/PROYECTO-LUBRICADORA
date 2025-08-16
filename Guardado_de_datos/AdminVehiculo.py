from .Conexion import *  # Importa la conexión a la base de datos desde el módulo Conexion

class manejarVehiculo:
    
    def MostrarVehiculo():
        try:
            # Crear una conexión con la base de datos
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()  # Crear un cursor para ejecutar consultas
            cursor.execute("SELECT * FROM vehiculo;")  # Ejecutar la consulta para seleccionar todos los registros de vehiculos
            resultado = cursor.fetchall()  # Obtener todos los registros resultantes
            conec.commit()  # Confirmar la transacción
            conec.close()  # Cerrar la conexión a la base de datos
            return resultado  # Retornar los resultados obtenidos

        except mysql.connector.Error as error:
            print("Error al intentar mostrar los datos {}".format(error))  # En caso de error, se muestra el mensaje

    # Método para insertar un nuevo vehiculo en la base de datos
    def IngresarVehiculo(placa, id_cliente, marca, color, modelo, año):
        try:
            # Crear una conexión con la base de datos
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()  # Crear un cursor para ejecutar consultas

            # SQL para insertar un nuevo vehiculo
            cursor.callproc("sp_insertar_vehiculo", (placa, id_cliente, marca, color, modelo, año))  # Valores a insertar

            # Ejecutar la consulta con los valores
            conec.commit()  # Confirmar la transacción
            print(cursor.rowcount, "Registro ingresado con exito")  # Informar si el registro fue exitoso
            conec.close()  # Cerrar la conexión a la base de datos

        except mysql.connector.Error as error:
            print("Error al intentar ingresar los datos {}".format(error))  # En caso de error, se muestra el mensaje

    # Método para modificar un empleado existente en la base de datos
    def ModificarVehiculo(placa_mod,placa_vieja, id_cliente, marca, color, modelo, año):
        try:
            # Crear una conexión con la base de datos
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()  # Crear un cursor para ejecutar consultas

            # SQL para actualizar los datos de un empleado
            cursor.callproc("sp_actualizar_vehiculo", (placa_vieja, placa_mod, id_cliente, marca, color, modelo, año))  # Valores a actualizar

            # Ejecutar la consulta con los valores
            conec.commit()  # Confirmar la transacción
            print(cursor.rowcount, "Registro modificado con exito")  # Informar si el registro fue modificado exitosamente
            conec.close()  # Cerrar la conexión a la base de datos

        except mysql.connector.Error as error:
            print("Error al intentar modificar los datos {}".format(error))  # En caso de error, se muestra el mensaje

    # Método para eliminar un vehiculo de la base de datos
    def EliminarVehiculo(placa):
        try:
            # Crear una conexión con la base de datos
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()  # Crear un cursor para ejecutar consultas

            # SQL para eliminar un vehiculo por su ID
            cursor.callproc("sp_actualizar_vehiculo", (placa))  # Valor del ID del vehiculo a eliminar

            # Ejecutar la consulta con el valor
            conec.commit()  # Confirmar la transacción
            print(cursor.rowcount, "Registro eliminado con exito")  # Informar si el registro fue eliminado exitosamente
            conec.close()  # Cerrar la conexión a la base de datos

        except mysql.connector.Error as error:
            print("Error al intentar eliminar los datos {}".format(error))  # En caso de error, se muestra el mensaje