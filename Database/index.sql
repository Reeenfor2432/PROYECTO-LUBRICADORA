USE LUBRICONTROL

/*La vista citasPendientes filtra por estado = 'pendiente'. 
Aumenta velocidad al consultar pendientes, en proceso, finalizadas o canceladas.*/
create index idx_cita_estado ON cita (estado);

/*Muchas vistas como citasClientesFrecuentes y citasTodas consultan JOIN cliente y JOIN empleado
También se hacen búsquedas de todas las citas de un cliente específico o un empleado.*/
create index idx_cliente_empleado ON cita (id_cliente, id_empleado);

/*La vista productosStockMenorCinco consulta WHERE stock < 5. Esto acelera el filtro 
al evitar escanear toda la tabla de producto*/
create index idx_producto_stock ON producto(stock);

/*Los vehículos se consultan casi siempre en relación a su dueño (JOIN cliente)
El indice acelera la busqueda del vehiculo y su cliente.*/
create index idx_vehiculo_cliente on vehiclo(id_cliente);

/*La vista facturaDetallada hace JOIN factura f ON f.cita = c.id_cita. Acelera el
join factura con cita*/
create index idx_factura_cita ON factura(cita);