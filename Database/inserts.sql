USE  LUBRICONTROL;

INSERT INTO cliente (cedula, nombre_cliente, telefono) VALUES
('0956321478', 'José Sánchez', '0998765432'),
('0912345678', 'María López', '0987654321'),
('0923456789', 'Carlos Vera', '0978563412'),
('0934567890', 'Diana Castillo', '0967451230'),
('0945678901', 'Luis Zambrano', '0956342871'),
('0954781234', 'Kevin Reinoso', '0998754312'),
('0923894738', 'Andrea Paredes', '0987234678'),
('0939123478', 'Marco Arce', '0978123478'),
('0967892345', 'Sofía Aguilar', '0967123456'),
('0912349876', 'Fernando Gavilánez', '0956347821');

INSERT INTO vehiculo (placa, id_cliente, marca, color, modelo, año) VALUES
('ABC0123', 100, 'Chevrolet', 'Blanco', 'Aveo Family', 2012),
('GHI3456', 101, 'Hyundai', 'Rojo', 'Accent', 2017),
('JKL6789', 102, 'Kia', 'Negro', 'Rio', 2018),
('MNO9012', 103, 'Toyota', 'Gris', 'Corolla', 2020),
('PQR2345', 104, 'Mazda', 'Azul', 'CX-5', 2021),
('STU3456', 105, 'Renault', 'Plomo', 'Logan', 2014),
('VWX6789', 106, 'Suzuki', 'Celeste', 'Swift', 2016),
('YZA9012', 107, 'Datsun', 'Rojo', 'Go+', 2019),
('BCD2345', 108, 'Nissan', 'Negro', 'Sentra', 2020),
('EFG5678', 109, 'Jeep', 'Verde', 'Compass', 2021);

INSERT INTO rol (nombre_rol, descripcion) VALUES
('Administrador', 'Gestiona el sistema completo'),
('Recepcionista', 'Recibe y agenda citas'),
('Mecánico', 'Realiza servicios técnicos'),
('Supervisor', 'Supervisa operaciones del taller'),
('Almacenero', 'Maneja inventario y productos');

INSERT INTO empleado (id_rol, nombre, telefono, domicilio) VALUES
(100, 'Andrés Cedeño', '0987451230', 'Cdla. Kennedy, Guayaquil'),
(101, 'Paola Romero', '0967123456', 'La Mariscal, Quito'),
(102, 'Esteban Cárdenas', '0998765412', 'Sauces 2, Guayaquil'),
(103, 'Lucía Muñoz', '0956743210', 'Centro Histórico, Cuenca'),
(104, 'David Jaramillo', '0981234567', 'Los Ceibos, Guayaquil'),
(100, 'Patricio Loor', '0995566123', 'La Garzota, Guayaquil'),
(101, 'Melanie Herrera', '0987345671', 'La Floresta, Quito'),
(102, 'Byron Villacís', '0978123904', 'La Atarazana, Guayaquil'),
(103, 'Natalia Jaramillo', '0967012345', 'La Libertad, Salinas'),
(104, 'Cristian Silva', '0956341234', 'Cdla. Los Vergeles, Guayaquil');

INSERT INTO servicio (nombre, descripcion, precio) VALUES
('Cambio de aceite', 'Reemplazo de aceite de motor', 25.00),
('Revisión de frenos', 'Chequeo y ajuste de frenos', 15.00),
('Alineación y balanceo', 'Ajuste de ruedas', 20.00),
('Limpieza de inyectores', 'Cambio de refrigerante', 30.00),
('Revisión general', 'Inspección completa del vehículo', 40.00),
('Cambio de filtro de aire', 'Reemplazo de filtro del motor', 10.00),
('Chequeo de batería', 'Medición y diagnóstico de batería', 5.00),
('Recarga de aire acondicionado', 'Recarga con gas refrigerante', 25.00),
('Rotación de llantas', 'Cambio de posición de neumáticos', 8.00),
('Diagnóstico computarizado', 'Lectura de códigos con scanner', 18.00);

INSERT INTO marca_producto (nombre_marca) VALUES
('Shell'),
('Mobil'),
('Castrol'),
('Valvoline'),
('Lubrax'),
('Gulf'),
('Repsol'),
('Total'),
('Petrobras'),
('Eni');

INSERT INTO categoria (nombre_categoria) VALUES
('Aceites'),
('Filtros'),
('Aditivos'),
('Refrigerantes'),
('Herramientas'),
('Filtros de aire'),
('Lubricantes para transmisión'),
('Líquidos de freno'),
('Aire acondicionado'),
('Accesorios');

INSERT INTO producto (nombre_producto, descripcion, precio_unitario, stock, id_marca, id_categoria) VALUES
('Aceite Shell Helix HX5 20W-50', 'Aceite mineral para motores a gasolina', 12.50, 50, 100, 100),
('Filtro de aceite Fram PH3614', 'Filtro compatible con vehículos Chevrolet', 5.00, 30, 101, 101),
('Aditivo STP Motor Flush', 'Limpieza interna del motor', 6.00, 25, 102, 102),
('Coolant Valvoline Verde', 'Refrigerante listo para usar', 8.00, 40, 103, 103),
('Llave para filtro de aceite', 'Herramienta de remoción', 7.50, 15, 104, 104),
('Aceite Gulf 10W-40', 'Lubricante semisintético para motores a gasolina', 14.00, 40, 105, 101),
('Filtro de aire Sakura', 'Filtro rectangular para vehículos Nissan', 6.50, 35, 106, 105),
('Líquido de frenos Total DOT-4', 'Para sistemas hidráulicos', 5.80, 20, 107, 107),
('Aditivo para aire acondicionado', 'Mejora el rendimiento del A/C', 9.50, 25, 108, 108),
('Ambientador de piña', 'Accesorio perfumado para cabina', 2.00, 60, 109, 109);

INSERT INTO cita (id_cliente, placa, id_empleado, hora_ingreso, hora_salida, estado) VALUES
(100, 'ABC0123', 100, '2025-07-27 09:00:00', '2025-07-27 10:00:00', 'finalizado'),
(101, 'GHI3456', 102, '2025-07-27 10:30:00', '2025-07-27 11:15:00', 'en_proceso'),
(102, 'JKL6789', 103, '2025-07-27 12:00:00', NULL, 'pendiente'),
(103, 'MNO9012', 104, '2025-07-28 08:00:00', NULL, 'pendiente'),
(104, 'PQR2345', 101, '2025-07-28 09:30:00', NULL, 'cancelado'),
(105, 'STU3456', 105, '2025-07-29 08:00:00', '2025-07-29 09:15:00', 'finalizado'),
(106, 'VWX6789', 106, '2025-07-29 09:30:00', NULL, 'en_proceso'),
(107, 'YZA9012', 107, '2025-07-29 10:30:00', NULL, 'pendiente'),
(108, 'BCD2345', 108, '2025-07-29 11:45:00', NULL, 'pendiente'),
(109, 'EFG5678', 109, '2025-07-29 13:00:00', NULL, 'cancelado');

INSERT INTO factura (cita, numero_factura, subtotal, total, impuesto, descuento) VALUES
(100, 'FAC-001', 25.00, 28.00, 3.00, 0.00),
(101, 'FAC-002', 20.00, 22.40, 2.40, 0.00),
(102, 'FAC-003', 30.00, 31.50, 1.50, 0.00),
(103, 'FAC-004', 40.00, 44.80, 4.80, 0.00),
(104, 'FAC-005', 12.00, 13.44, 1.44, 0.00),
(105, 'FAC-006', 25.00, 28.00, 3.00, 0.00),
(106, 'FAC-007', 15.00, 16.80, 1.80, 0.00),
(107, 'FAC-008', 40.00, 44.80, 4.80, 0.00),
(108, 'FAC-009', 12.00, 13.44, 1.44, 0.00),
(109, 'FAC-010', 18.00, 20.16, 2.16, 0.00);

INSERT INTO producto_usado (id_cita, id_producto, cantidad) VALUES
(100, 100, 1),
(101, 101, 1),
(102, 102, 2),
(103, 103, 1),
(100, 104, 1),
(105, 105, 1),
(106, 106, 1),
(107, 107, 1),
(108, 108, 1),
(109, 109, 1);

INSERT INTO Detalle_Servicio (id_cita, id_servicio, id_empleado) VALUES
(100, 100, 102),
(101, 102, 103),
(102, 103, 102),
(103, 104, 104),
(104, 101, 100),
(105, 105, 105),
(106, 106, 106),
(107, 107, 107),
(108, 108, 108),
(109, 109, 109);

