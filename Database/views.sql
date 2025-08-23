use LUBRICONTROL;

CREATE VIEW facturaDetallada AS
SELECT f.id_factura,f.subtotal,f.impuesto,f.descuento,f.total,c.id_cita,cli.nombre_cliente,cli.cedula,v.placa
FROM factura f
JOIN cita c ON f.cita = c.id_cita
JOIN cliente cli ON c.id_cliente = cli.id_cliente
JOIN vehiculo v ON c.placa = v.placa;

CREATE VIEW productosStockMenorCinco AS
SELECT p.id_producto,p.nombre_producto,descripcion, p.precio_unitario, p.stock, m.nombre_marca, c.nombre_categoria 
FROM producto p 
JOIN marca_producto m USING (id_marca)
JOIN categoria c USING (id_categoria) 
WHERE p.stock < 5;

CREATE VIEW citasClientesFrecuentes AS
SELECT c.id_cita,c.id_cliente,cl.nombre_cliente,cl.cedula,c.placa,c.id_empleado,e.nombre AS nombre_empleado,c.hora_ingreso,c.hora_salida,c.estado
FROM cita c
JOIN cliente cl ON c.id_cliente = cl.id_cliente
JOIN empleado e ON c.id_empleado = e.id_empleado
WHERE c.id_cliente IN (
    SELECT id_cliente
    FROM cita
    GROUP BY id_cliente
    HAVING COUNT(*) > 5);

CREATE VIEW citasPendientes AS
SELECT c.id_cita,c.id_cliente,cl.nombre_cliente,cl.cedula,c.placa,c.id_empleado,e.nombre AS nombre_empleado,c.hora_ingreso,c.hora_salida,c.estado
FROM cita c
JOIN cliente cl ON c.id_cliente = cl.id_cliente
JOIN empleado e ON c.id_empleado = e.id_empleado
WHERE estado = "pendiente";

CREATE VIEW citasTodas AS
SELECT c.id_cita,c.id_cliente,cl.nombre_cliente,cl.cedula,c.placa,c.id_empleado,e.nombre AS nombre_empleado,c.hora_ingreso,c.hora_salida,c.estado
FROM cita c
JOIN cliente cl ON c.id_cliente = cl.id_cliente
JOIN empleado e ON c.id_empleado = e.id_empleado;