USE  LUBRICONTROL;

DELIMITER $$
CREATE TRIGGER disminución_producto AFTER INSERT ON cliente
FOR EACH ROW
BEGIN
    INSERT INTO auditoria_cliente (id_cliente, accion, fecha, usuario)
    VALUES (NEW.id_cliente, 'INSERT', NOW(), USER());
END$$
DELIMITER ;