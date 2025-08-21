USE LUBRICONTROL;

/* CLIENTE INSERTAR, MODIFICAR, ELIMINAR*/
DELIMITER $$
CREATE PROCEDURE sp_insertar_cliente(in p_cedula char(10), p_nombre varchar(60), p_telefono varchar(15) )
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error insertando cliente';
    END;

    START TRANSACTION;
    
    IF LENGTH(p_cedula) <> 10 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cédula inválida';
    END IF;

    INSERT INTO cliente (id_cliente, cedula, nombre_cliente, telefono)
    VALUES (null, p_cedula, p_nombre, p_telefono);

    COMMIT;
END
$$DELIMITER 

DELIMITER $$
CREATE PROCEDURE sp_actualizar_cliente(IN p_id INT,IN p_cedula CHAR(10),IN p_nombre CHAR(60),IN p_telefono VARCHAR(15))
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error actualizando cliente';
    END;

    START TRANSACTION;

    IF NOT EXISTS (SELECT 1 FROM cliente WHERE id_cliente = p_id) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cliente no encontrado';
    END IF;

    UPDATE cliente
    SET cedula = p_cedula, nombre_cliente = p_nombre, telefono = p_telefono
    WHERE id_cliente = p_id;

    COMMIT;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE sp_eliminar_cliente(IN p_id INT)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error eliminando cliente';
    END;

    START TRANSACTION;

    IF NOT EXISTS (SELECT 1 FROM cliente WHERE id_cliente = p_id) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cliente no encontrado';
    END IF;

    DELETE FROM cliente WHERE id_cliente = p_id;

    COMMIT;
END
$$DELIMITER ;

/** EMPLEADO INSERTAR, MODIFICAR, ELIMINAR**/
DELIMITER $$
create procedure sp_insertar_empleado(p_rol INT, p_nombre varchar(60), p_telefono varchar(15), p_domicilio varchar(100) )
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error insertando empleado';
    END;

    START TRANSACTION;

    IF NOT EXISTS (SELECT 1 FROM rol WHERE id_rol = p_rol) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Rol no existe';
    END IF;

    INSERT INTO empleado
    VALUES (null, p_rol, p_nombre, p_telefono, p_domicilio);

    COMMIT;
END
$$DELIMITER 

DELIMITER $$
CREATE PROCEDURE sp_actualizar_empleado(empleado INT, rol INT nom varchar(60), tel varchar(15), dom varchar(100))
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error actualizando empleado';
    END;

    START TRANSACTION;

    IF NOT EXISTS (SELECT 1 FROM cliente WHERE id_empleado = empleado) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Empleado no encontrado';
    END IF;

    UPDATE cliente
    SET id_rol = rol, nombre = nom, telefono = tel, domicilio= dom
    WHERE id_empleado = empleado;

    COMMIT;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE sp_eliminar_empleado(IN p_id INT)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error eliminando cliente';
    END;

    START TRANSACTION;

    IF NOT EXISTS (SELECT 1 FROM empelado WHERE id_empleado = p_id) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Empleado no encontrado';
    END IF;

    DELETE FROM empleado WHERE id_empleado = p_id;

    COMMIT;
END
$$DELIMITER ;

/** VEHICULO MODIFICAR, INSERTAR, ELIMINAR**/
DELIMITER $$
CREATE PROCEDURE sp_insertar_vehiculo(IN p_placa CHAR(7),IN p_id_cliente INT,IN p_marca VARCHAR(20),IN p_color VARCHAR(20),IN p_modelo VARCHAR(40),IN p_año YEAR)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error insertando vehiculo';
    END;

    START TRANSACTION;

    IF NOT EXISTS (SELECT 1 FROM cliente WHERE id_cliente = p_id_cliente) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cliente no existe';
    END IF;

    INSERT INTO vehiculo (placa, id_cliente, marca, color, modelo, año)
    VALUES (p_placa, p_id_cliente, p_marca, p_color, p_modelo, p_año);

    COMMIT;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE sp_actualizar_vehiculo(IN p_placa_old, IN p_placa CHAR(7),IN p_id_cliente INT,IN p_marca VARCHAR(20),IN p_color VARCHAR(20),IN p_modelo VARCHAR(40),IN p_anio YEAR)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error actualizando vehiculo';
    END;

    START TRANSACTION;

    IF NOT EXISTS (SELECT 1 FROM vehiculo WHERE placa = p_placa_old) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Vehiculo no encontrado';
    END IF;

    UPDATE vehiculo
    SET placa = p_placa, id_cliente = p_id_cliente, marca = p_marca, color = p_color,
        modelo = p_modelo, año = p_anio
    WHERE placa = p_placa_old;

    COMMIT;
END
$$ DELIMITER ;

DELIMITER $$
CREATE PROCEDURE sp_eliminar_vehiculo(IN p_placa CHAR(7))
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error eliminando vehiculo';
    END;

    START TRANSACTION;

    IF NOT EXISTS (SELECT 1 FROM vehiculo WHERE placa = p_placa) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Vehiculo no encontrado';
    END IF;

    DELETE FROM vehiculo WHERE placa = p_placa;

    COMMIT;
END
$$DELIMITER ;


/** ROL MODIFICAR, INSERTAR, ELIMINAR**/
DELIMITER $$
CREATE PROCEDURE sp_insertar_rol(IN p_nombre VARCHAR(30),IN p_descripcion VARCHAR(300))
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error insertando rol';
    END;

    START TRANSACTION;

    INSERT INTO rol (nombre_rol, descripcion)
    VALUES (p_nombre, p_descripcion);

    COMMIT;
END
$$DELIMITER ;

DELIMITER $$
CREATE PROCEDURE sp_actualizar_rol(
    IN p_id INT,
    IN p_nombre VARCHAR(30),
    IN p_descripcion VARCHAR(300)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error actualizando rol';
    END;

    START TRANSACTION;

    IF NOT EXISTS (SELECT 1 FROM rol WHERE id_rol = p_id) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Rol no encontrado';
    END IF;

    UPDATE rol
    SET nombre_rol = p_nombre, descripcion = p_descripcion
    WHERE id_rol = p_id;

    COMMIT;
END
$$DELIMITER ;

DELIMITER $$
CREATE PROCEDURE sp_eliminar_rol(IN p_id INT)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error eliminando rol';
    END;

    START TRANSACTION;

    IF NOT EXISTS (SELECT 1 FROM rol WHERE id_rol = p_id) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Rol no encontrado';
    END IF;

    DELETE FROM rol WHERE id_rol = p_id;

    COMMIT;
END
$$DELIMITER ;


/** SERVICIO MODIFICAR, INSERTAR, ELIMINAR**/
DELIMITER $$
CREATE PROCEDURE sp_insertar_servicio(IN p_nombre VARCHAR(100),IN p_desc VARCHAR(100),IN p_precio DECIMAL(8,2)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error insertando servicio';
    END;

    START TRANSACTION;

    INSERT INTO servicio (nombre, descripcion, precio)
    VALUES (p_nombre, p_desc, p_precio);

    COMMIT;
END
$$DELIMITER ;

DELIMITER $$
CREATE PROCEDURE sp_actualizar_servicio(IN p_id INT,IN p_nombre VARCHAR(100),IN p_desc VARCHAR(100),IN p_precio DECIMAL(8,2))
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error actualizando servicio';
    END;

    START TRANSACTION;

    IF NOT EXISTS (SELECT 1 FROM servicio WHERE id_servicio = p_id) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Servicio no encontrado';
    END IF;

    UPDATE servicio
    SET nombre = p_nombre, descripcion = p_desc, precio = p_precio
    WHERE id_servicio = p_id;

    COMMIT;
END
$$DELIMITER ;

DELIMITER $$
CREATE PROCEDURE sp_eliminar_servicio(IN p_id INT)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error eliminando servicio';
    END;

    START TRANSACTION;

    IF NOT EXISTS (SELECT 1 FROM servicio WHERE id_servicio = p_id) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Servicio no encontrado';
    END IF;

    DELETE FROM servicio WHERE id_servicio = p_id;

    COMMIT;
END
$$DELIMITER ;


/** MARCA MODIFICAR, INSERTAR, ELIMINAR**/

DELIMITER $$
CREATE PROCEDURE sp_insertar_marca(IN p_nombre VARCHAR(40))
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error insertando marca';
    END;

    START TRANSACTION;

    INSERT INTO marca_producto (nombre_marca)
    VALUES (p_nombre);

    COMMIT;
END
$$DELIMITER ;

DELIMITER $$
CREATE PROCEDURE sp_actualizar_marca(IN p_id INT,IN p_nombre VARCHAR(40))
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error actualizando marca';
    END;

    START TRANSACTION;

    IF NOT EXISTS (SELECT 1 FROM marca_producto WHERE id_marca = p_id) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Marca no encontrada';
    END IF;

    UPDATE marca_producto
    SET nombre_marca = p_nombre
    WHERE id_marca = p_id;

    COMMIT;
END
$$DELIMITER ;

DELIMITER $$
CREATE PROCEDURE sp_eliminar_marca(IN p_id INT)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error eliminando marca';
    END;

    START TRANSACTION;

    IF NOT EXISTS (SELECT 1 FROM marca_producto WHERE id_marca = p_id) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Marca no encontrada';
    END IF;

    DELETE FROM marca_producto WHERE id_marca = p_id;

    COMMIT;
END
$$DELIMITER ;


/** CATEGORIA MODIFICAR, INSERTAR, ELIMINAR**/
DELIMITER $$
CREATE PROCEDURE sp_insertar_categoria(IN p_nombre VARCHAR(40))
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error insertando categoria';
    END;

    START TRANSACTION;

    INSERT INTO categoria (nombre_categoria)
    VALUES (p_nombre);

    COMMIT;
END
$$DELIMITER ;

DELIMITER $$
CREATE PROCEDURE sp_actualizar_categoria(IN p_id INT,IN p_nombre VARCHAR(40))
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error actualizando categoria';
    END;

    START TRANSACTION;

    IF NOT EXISTS (SELECT 1 FROM categoria WHERE id_categoria = p_id) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Categoria no encontrada';
    END IF;

    UPDATE categoria
    SET nombre_categoria = p_nombre
    WHERE id_categoria = p_id;

    COMMIT;
END
$$DELIMITER ;

DELIMITER $$
CREATE PROCEDURE sp_eliminar_categoria(IN p_id INT)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error eliminando categoria';
    END;

    START TRANSACTION;

    IF NOT EXISTS (SELECT 1 FROM categoria WHERE id_categoria = p_id) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Categoria no encontrada';
    END IF;

    DELETE FROM categoria WHERE id_categoria = p_id;

    COMMIT;
END
$$DELIMITER ;


/** PRODUCTO MODIFICAR, INSERTAR, ELIMINAR**/
DELIMITER $$
CREATE PROCEDURE sp_insertar_producto(IN p_nombre VARCHAR(60),IN p_desc VARCHAR(100),IN p_precio DECIMAL(8,2),IN p_stock INT,IN p_id_marca INT,IN p_id_categoria INT)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error insertando producto';
    END;

    START TRANSACTION;

    IF NOT EXISTS (SELECT 1 FROM marca_producto WHERE id_marca = p_id_marca) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Marca no existe';
    END IF;

    IF NOT EXISTS (SELECT 1 FROM categoria WHERE id_categoria = p_id_categoria) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Categoria no existe';
    END IF;

    INSERT INTO producto (nombre_producto, descripcion, precio_unitario, stock, id_marca, id_categoria)
    VALUES (p_nombre, p_desc, p_precio, p_stock, p_id_marca, p_id_categoria);

    COMMIT;
END
$$DELIMITER ;

DELIMITER $$
CREATE PROCEDURE sp_actualizar_producto(IN p_id INT,IN p_nombre VARCHAR(60),IN p_desc VARCHAR(100),IN p_precio DECIMAL(8,2),IN p_stock INT,IN p_id_marca INT,IN p_id_categoria INT)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error actualizando producto';
    END;

    START TRANSACTION;

    IF NOT EXISTS (SELECT 1 FROM producto WHERE id_producto = p_id) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Producto no encontrado';
    END IF;

    UPDATE producto
    SET nombre_producto = p_nombre, descripcion = p_desc, precio_unitario = p_precio,
        stock = p_stock, id_marca = p_id_marca, id_categoria = p_id_categoria
    WHERE id_producto = p_id;

    COMMIT;
END
$$DELIMITER ;

DELIMITER $$
CREATE PROCEDURE sp_eliminar_producto(IN p_id INT)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error eliminando producto';
    END;

    START TRANSACTION;

    IF NOT EXISTS (SELECT 1 FROM producto WHERE id_producto = p_id) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Producto no encontrado';
    END IF;

    DELETE FROM producto WHERE id_producto = p_id;

    COMMIT;
END
$$DELIMITER ;


/** CITA MODIFICAR, INSERTAR, ELIMINAR**/
DELIMITER $$
CREATE PROCEDURE sp_insertar_cita(IN p_id_cliente INT,IN p_placa CHAR(7),IN p_id_empleado INT,IN p_hora_ingreso DATETIME,IN p_hora_salida DATETIME,IN p_estado ENUM('pendiente','en_proceso','finalizado','cancelado'))
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error insertando cita';
    END;

    START TRANSACTION;

    IF NOT EXISTS (SELECT 1 FROM cliente WHERE id_cliente = p_id_cliente) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cliente no existe';
    END IF;

    IF NOT EXISTS (SELECT 1 FROM vehiculo WHERE placa = p_placa) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Vehiculo no existe';
    END IF;

    IF NOT EXISTS (SELECT 1 FROM empleado WHERE id_empleado = p_id_empleado) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Empleado no existe';
    END IF;

    INSERT INTO cita (id_cliente, placa, id_empleado, hora_ingreso, hora_salida, estado)
    VALUES (p_id_cliente, p_placa, p_id_empleado, p_hora_ingreso, p_hora_salida, p_estado);

    COMMIT;
END
$$DELIMITER ;

DELIMITER $$
CREATE PROCEDURE sp_actualizar_cita(IN p_id INT,IN p_hora_salida DATETIME,IN p_estado ENUM('pendiente','en_proceso','finalizado','cancelado'))
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error actualizando cita';
    END;

    START TRANSACTION;

    IF NOT EXISTS (SELECT 1 FROM cita WHERE id_cita = p_id) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cita no encontrada';
    END IF;

    UPDATE cita
    SET hora_salida = p_hora_salida, estado = p_estado
    WHERE id_cita = p_id;

    COMMIT;
END
$$DELIMITER ;

DELIMITER $$
CREATE PROCEDURE sp_eliminar_cita(IN p_id INT)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error eliminando cita';
    END;

    START TRANSACTION;

    IF NOT EXISTS (SELECT 1 FROM cita WHERE id_cita = p_id) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cita no encontrada';
    END IF;

    DELETE FROM cita WHERE id_cita = p_id;

    COMMIT;
END
$$DELIMITER ;

/* FACTURA INSERTAR (NO MODIFICABLE NI ELIMINABLE) */
DELIMITER $$

CREATE PROCEDURE sp_insertar_factura(IN p_cita INT,IN p_subtotal DECIMAL(10,2),IN p_total DECIMAL(10,2),IN p_impuesto DECIMAL(5,2),IN p_descuento DECIMAL(5,2))
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al insertar la factura';
    END;

    START TRANSACTION;

    IF (SELECT COUNT(*) FROM cita WHERE id_cita = p_cita) = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La cita indicada no existe, no se puede generar factura';
    END IF;


    INSERT INTO factura (cita, subtotal, total, impuesto, descuento)
    VALUES (p_cita, p_subtotal, p_total, p_impuesto, p_descuento);

    COMMIT;
END 
$$DELIMITER ;





