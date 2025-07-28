from .Conexion import *  # Importa la conexión a la base de datos desde el módulo Conexion

class Aggclientes:
    
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
            cursor = conec.cursor()  # Crear un cursor para ejecutar consultas

            # SQL para insertar un nuevo cliente
            sql = "insert into cliente values(null,%s,%s,%s);"
            valores = (cedula, nombre, telefono)  # Valores a insertar

            # Ejecutar la consulta con los valores
            cursor.execute(sql, valores)
            conec.commit()  # Confirmar la transacción
            print(cursor.rowcount, "Registro ingresado con exito")  # Informar si el registro fue exitoso
            conec.close()  # Cerrar la conexión a la base de datos

        except mysql.connector.Error as error:
            print("Error al intentar ingresar los datos {}".format(error))  # En caso de error, se muestra el mensaje

    # Método para modificar un cliente existente en la base de datos
    def ModificarClientes(id, cedula, nombre, telefono):
        try:
            # Crear una conexión con la base de datos
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()  # Crear un cursor para ejecutar consultas

            # SQL para actualizar los datos de un cliente
            sql = "UPDATE cliente SET cedula=%s,nombre_cliente=%s, telefono=%s WHERE id_cliente=%s;"
            valores = (cedula, nombre, telefono, id)  # Valores a actualizar

            # Ejecutar la consulta con los valores
            cursor.execute(sql, valores)
            conec.commit()  # Confirmar la transacción
            print(cursor.rowcount, "Registro modificado con exito")  # Informar si el registro fue modificado exitosamente
            conec.close()  # Cerrar la conexión a la base de datos

        except mysql.connector.Error as error:
            print("Error al intentar modificar los datos {}".format(error))  # En caso de error, se muestra el mensaje

    # Método para eliminar un cliente de la base de datos
    def EliminarClientes(id):
        try:
            # Crear una conexión con la base de datos
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()  # Crear un cursor para ejecutar consultas

            # SQL para eliminar un cliente por su ID
            sql = "DELETE FROM cliente WHERE id_cliente=%s;"
            valores = (id,)  # Valor del ID del cliente a eliminar

            # Ejecutar la consulta con el valor
            cursor.execute(sql, valores)
            conec.commit()  # Confirmar la transacción
            print(cursor.rowcount, "Registro eliminado con exito")  # Informar si el registro fue eliminado exitosamente
            conec.close()  # Cerrar la conexión a la base de datos

        except mysql.connector.Error as error:
            print("Error al intentar eliminar los datos {}".format(error))  # En caso de error, se muestra el mensaje
