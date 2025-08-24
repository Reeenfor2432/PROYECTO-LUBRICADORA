CREATE USER 'admin_lubri'@'%' IDENTIFIED BY 'Admin123*' PASSWORD EXPIRE;
GRANT ALL PRIVILEGES ON lubricontrol.* TO 'admin_lubri'@'%';

CREATE USER 'inventario_lubri'@'%' IDENTIFIED BY 'Inv123*' PASSWORD EXPIRE;
GRANT SELECT, INSERT, UPDATE ON lubricontrol.producto TO 'inventario_lubri'@'%';
GRANT SELECT ON lubricontrol.productosStockMenorCinco TO 'inventario_lubri'@'%';
GRANT EXECUTE ON PROCEDURE lubricontrol.sp_actualizar_producto TO 'inventario_lubri'@'%';

CREATE USER 'citas_lubri'@'%' IDENTIFIED BY 'Citas123*' PASSWORD EXPIRE;
GRANT SELECT, INSERT, UPDATE ON lubricontrol.cita TO 'citas_lubri'@'%';
GRANT SELECT ON lubricontrol.citasPendientes TO 'citas_lubri'@'%';
GRANT SELECT ON lubricontrol.citasClientesFrecuentes TO 'citas_lubri'@'%';
GRANT EXECUTE ON PROCEDURE lubricontrol.sp_insertar_cita TO 'citas_lubri'@'%';

CREATE USER 'sistemas_lubri'@'%' IDENTIFIED BY 'Sys123*' PASSWORD EXPIRE;
GRANT SELECT, INSERT, UPDATE, DELETE ON lubricontrol.empleado TO 'sistemas_lubri'@'%';
GRANT SELECT, INSERT, UPDATE, DELETE ON lubricontrol.rol TO 'sistemas_lubri'@'%';
GRANT EXECUTE ON PROCEDURE lubricontrol.sp_actualizar_empleado TO 'sistemas_lubri'@'%';
GRANT EXECUTE ON PROCEDURE lubricontrol.sp_actualizar_rol TO 'sistemas_lubri'@'%';

CREATE USER 'facturacion_lubri'@'%' IDENTIFIED BY 'Fact123*' PASSWORD EXPIRE;
GRANT SELECT, INSERT ON lubricontrol.factura TO 'facturacion_lubri'@'%';
GRANT SELECT ON lubricontrol.facturaDetallada TO 'facturacion_lubri'@'%';
GRANT EXECUTE ON PROCEDURE lubricontrol.sp_insertar_factura TO 'facturacion_lubri'@'%';

FLUSH PRIVILEGES;


