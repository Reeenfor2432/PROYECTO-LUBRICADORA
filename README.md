# PROYECTO-LUBRICADORA
LubriControl — Gestión de lubricadora

Sistema académico de gestión para una lubricadora. Permite administrar clientes, vehículos, empleados, servicios, roles, inventario y citas (orden de trabajo); además genera reportes y facturas.

Está desarrollada con Python (Tkinter) para la interfaz y MySQL como motor de base de datos.

Requisitos

Python 3.11+ (probado también en 3.13).

Paquete: mysql-connector-python.

Reportes (implementados/plan)
Ingresos por mes.
Servicios más solicitados.
Productos por agotarse (desde inventario).
Desempeño por empleado.
(La consulta y visualización se invocan desde vistaReporte.py.)

Decisiones de diseño
IDs naturales: cédula e identificación de vehículo como PK del negocio (acorde al proceso real).
Descuento: se calcula y guarda en la cita (campo descuento), para mantener trazabilidad del total final.

Uso académico. No apto para producción sin revisión de seguridad y cumplimiento.

