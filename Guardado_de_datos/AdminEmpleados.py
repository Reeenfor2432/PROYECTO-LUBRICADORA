from .Conexion import *  # Importa la conexión a la base de datos desde el módulo Conexion

class manejarEmpleado:
    
    # Método para mostrar todos los clientes en la base de datos
    def MostrarEmpleado():
        try:
            # Crear una conexión con la base de datos
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()  # Crear un cursor para ejecutar consultas
            cursor.execute("SELECT * FROM empleado;")  # Ejecutar la consulta para seleccionar todos los registros de empleados
            resultado = cursor.fetchall()  # Obtener todos los registros resultantes
            conec.commit()  # Confirmar la transacción
            conec.close()  # Cerrar la conexión a la base de datos
            return resultado  # Retornar los resultados obtenidos

        except mysql.connector.Error as error:
            print("Error al intentar mostrar los datos {}".format(error))  # En caso de error, se muestra el mensaje

    # Método para insertar un nuevo empleado en la base de datos
    def IngresarEmpleados(id_rol, nombre, telefono, domicilio):
        try:
            # Crear una conexión con la base de datos
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()  # Crear un cursor para ejecutar consultas

            # SQL para insertar un nuevo empleado
            cursor.callproc("sp_insertar_empleado", (id_rol, nombre, telefono, domicilio))

            conec.commit()  # Confirmar la transacción
            print(cursor.rowcount, "Registro ingresado con exito")  # Informar si el registro fue exitoso
            conec.close()  # Cerrar la conexión a la base de datos

        except mysql.connector.Error as error:
            print("Error al intentar ingresar los datos {}".format(error))  # En caso de error, se muestra el mensaje

    # Método para modificar un empleado existente en la base de datos
    def ModificarEmpleados(id, id_rol, nombre, telefono,domicilio):
        try:
            # Crear una conexión con la base de datos
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()  # Crear un cursor para ejecutar consultas

            # SQL para actualizar los datos de un empleado
            cursor.callproc("sp_actualizar_empleado", (id,id_rol, nombre, telefono, domicilio))

            # Ejecutar la consulta con los valores
            conec.commit()  # Confirmar la transacción
            print(cursor.rowcount, "Registro modificado con exito")  # Informar si el registro fue modificado exitosamente
            conec.close()  # Cerrar la conexión a la base de datos

        except mysql.connector.Error as error:
            print("Error al intentar modificar los datos {}".format(error))  # En caso de error, se muestra el mensaje

    # Método para eliminar un empleado de la base de datos
    def EliminarEmpleados(id):
        try:
            # Crear una conexión con la base de datos
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()  # Crear un cursor para ejecutar consultas

            # SQL para eliminar un empleado por su ID
            cursor.callproc("sp_eliminar_empleado", (id))

            # Ejecutar la consulta con el valor
            conec.commit()  # Confirmar la transacción
            print(cursor.rowcount, "Registro eliminado con exito")  # Informar si el registro fue eliminado exitosamente
            conec.close()  # Cerrar la conexión a la base de datos

        except mysql.connector.Error as error:
            print("Error al intentar eliminar los datos {}".format(error))  # En caso de error, se muestra el mensaje