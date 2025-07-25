CREATE DATABASE LUBRICONTROL;

CREATE TABLE cliente (
	cedula CHAR(10) PRIMARY KEY,
	nombre_cliente VARCHAR(60),
	telefono VARCHAR(15),
	frecuente TINYINT(1)
);

CREATE TABLE vehiculo(
	placa CHAR(7) PRIMARY KEY,
	cedula CHAR(7),
	marca VARCHAR(20),
	color VARCHAR(20),
	modelo VARCHAR(40),
	año YEAR,
	FOREIGN KEY(cedula) REFERENCES cliente(cedula)
);

CREATE TABLE factura(
	id_factura INT AUTO_INCREMENT PRIMARY KEY,
	cita INT,
	numero_factura VARCHAR(60),
	subtotal DECIMAL(10,2),
	total DECIMAL(10,2),
	impuesto DECIMAL(5,2),
	descuento DECIMAL(5,2),
	FOREIGN KEY(cita) REFERENCES cita(id_cita)
);

CREATE TABLE empleado(
	id_empleado INT AUTO_INCREMENT PRIMARY KEY,
	id_rol INT,
	nombre VARCHAR(60),
	telefono VARCHAR(15),
	domicilio VARCHAR(100),
	FOREIGN KEY(id_rol) REFERENCES rol(id_rol)
);

CREATE TABLE rol (
	id_rol INT AUTO_INCREMENT PRIMARY KEY,
	nombre_rol VARCHAR(30),
	descripcion VARCHAR(300)
);

CREATE TABLE Detalle_Servicio (
	id_cita INT,
	id_servicio INT,
	id_empleado INT,
	PRIMARY KEY (id_cita, id_servicio, id_empleado),
	FOREIGN KEY (id_cita) REFERENCES citas(id_cita),
	FOREIGN KEY (id_servicio) REFERENCES Servicios(id_servicio),
	FOREIGN KEY (id_empleado) REFERENCES Empleados(id_empleado)
);

CREATE TABLE servicio (
	id_servicio INT AUTO_INCREMENT PRIMARY KEY,
	nombre VARCHAR(100),
	descripcion VARCHAR(100),
	precio DECIMAL(8,2)
);

CREATE TABLE producto(
	id_producto INT AUTO_INCREMENT PRIMARY KEY,
	nombre_producto VARCHAR(60),
	descripcion VARCHAR(100),
	precio_unitario DECIMAL(8,2),
	stock INT, 
	id_marca INT,
	id_categoria INT,
	FOREIGN KEY(id_marca) REFERENCES marca_producto(id_marca),
	FOREIGN KEY(id_categoria) REFERENCES categoria(id_categoria)
);

CREATE TABLE marca_producto(
	id_marca VARCHAR(14) AUTO_INCREMENT PRIMARY KEY ,
	nombre_marca VARCHAR(40)
);

CREATE TABLE categoria(
	id_categoria INT AUTO_INCREMENT PRIMARY KEY ,
	nombre_categoria VARCHAR(40)
);

CREATE TABLE producto_usado(
	id_cita INT,
	id_producto INT,
	cantidad INT,
	PRIMARY KEY(id_cita,id_producto),
	FOREIGN KEY(id_cita) REFERENCES cita(id_cita),
	FOREIGN KEY(id_producto) REFERENCES producto(id_producto)
);

CREATE TABLE cita(
	id_cita INT AUTO_INCREMENT PRIMARY KEY,
	cedula CHAR(10),
	placa CHAR(7),
	id_empleado INT,
	hora_ingreso DATETIME,
	hora_salida DATETIME,
	estado ENUM('pendiente','en_proceso','finalizado','cancelado'),
	FOREIGN KEY(cedula) REFERENCES clientes(cedula),
	FOREIGN KEY(placa) REFERENCES vehiculo(placa),
	FOREIGN KEY(id_empleado) REFERENCES empleados(id_empleado)
);