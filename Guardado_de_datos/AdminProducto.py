from .Conexion import *  # Importa la conexión a la base de datos desde el módulo Conexion

class manejarProducto:
    
    def MostrarProducto():
        try:
            # Crear una conexión con la base de datos
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()  # Crear un cursor para ejecutar consultas
            cursor.execute("SELECT * FROM producto;")  # Ejecutar la consulta para seleccionar todos los registros de productos
            resultado = cursor.fetchall()  # Obtener todos los registros resultantes
            conec.commit()  # Confirmar la transacción
            conec.close()  # Cerrar la conexión a la base de datos
            return resultado  # Retornar los resultados obtenidos

        except mysql.connector.Error as error:
            print("Error al intentar mostrar los datos {}".format(error))  # En caso de error, se muestra el mensaje

    # Método para insertar un nuevo vehiculo en la base de datos
    def IngresarProducto(nombre_producto, descripcion, precio, stock,id_marca, id_categoria):
        try:
            # Crear una conexión con la base de datos
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()  # Crear un cursor para ejecutar consultas

            # SQL para insertar un nuevo producto
            cursor.callproc("sp_insertar_producto", (nombre_producto, descripcion, precio, stock,id_marca, id_categoria))  # Valores a insertar

            # Ejecutar la consulta con los valores
            conec.commit()  # Confirmar la transacción
            print(cursor.rowcount, "Registro ingresado con exito")  # Informar si el registro fue exitoso
            conec.close()  # Cerrar la conexión a la base de datos

        except mysql.connector.Error as error:
            print("Error al intentar ingresar los datos {}".format(error))  # En caso de error, se muestra el mensaje

    # Método para modificar un producto existente en la base de datos
    def ModificarProducto(id_producto, nombre_producto, descripcion, precio, stock, id_marca, id_categoria):
        try:
            # Crear una conexión con la base de datos
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()  # Crear un cursor para ejecutar consultas

            # SQL para actualizar los datos de un empleado
            cursor.callproc("sp_actualizar_producto", (id_producto,nombre_producto, descripcion, precio, stock,id_marca, id_categoria))

            # Ejecutar la consulta con los valores
            conec.commit()  # Confirmar la transacción
            print(cursor.rowcount, "Registro modificado con exito")  # Informar si el registro fue modificado exitosamente
            conec.close()  # Cerrar la conexión a la base de datos

        except mysql.connector.Error as error:
            print("Error al intentar modificar los datos {}".format(error))  # En caso de error, se muestra el mensaje

    # Método para eliminar un vehiculo de la base de datos
    def EliminarProducto(id_producto):
        try:
            # Crear una conexión con la base de datos
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()  # Crear un cursor para ejecutar consultas

            # SQL para eliminar un vehiculo por su ID
            cursor.callproc("sp_eliminar_producto", (int(id_producto),))

            # Ejecutar la consulta con el valor
            conec.commit()  # Confirmar la transacción
            print(cursor.rowcount, "Registro eliminado con exito")  # Informar si el registro fue eliminado exitosamente
            conec.close()  # Cerrar la conexión a la base de datos

        except mysql.connector.Error as error:
            print("Error al intentar eliminar los datos {}".format(error))  # En caso de error, se muestra el mensaje
        
    @staticmethod
    def obtenerId_marca(nombre_marca):
        # Crear una conexión con la base de datos
        try:
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()  # Crear un cursor para ejecutar consultas
            sql = "SELECT id_marca FROM marca_producto WHERE nombre_marca = %s"
            cursor.execute(sql, (nombre_marca,))
            resultado = cursor.fetchone()

            # Verificar si se encontró una marca
            if resultado:
                id_marca = resultado[0]  # Devuelve el id
            else:
                sql_insertar = "INSERT INTO marca_producto (nombre_marca) VALUES (%s)"
                cursor.execute(sql_insertar, (nombre_marca,))
                conec.commit()  # Marca no encontrada, entonces se añade
                id_marca = cursor.lastrowid
            cursor.close()
            conec.close()
            return id_marca

        except mysql.connector.Error as error:
            print("Error al conectar {}".format(error))
    
    @staticmethod
    def obtenerId_categoria(nombre_categoria):
        # Crear una conexión con la base de datos
        try:
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()  
            sql = "SELECT id_categoria FROM categoria WHERE nombre_categoria = %s"
            cursor.execute(sql, (nombre_categoria,))
            resultado = cursor.fetchone()

            # Verificar si se encontró una categoria
            if resultado:
                id_categoria = resultado[0]  # Devuelve el id
            else:
                cursor.callproc("sp_insertar_categoria", (nombre_categoria,))
                conec.commit()  # Categoria no encontrada, entonces se añade
                id_categoria = cursor.lastrowid
            cursor.close()
            conec.close()
            return id_categoria

        except mysql.connector.Error as error:
            print("Error al conectar {}".format(error))
