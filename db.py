# db.py  – puente único para todas las vistas
from Guardado_de_datos.Conexion import CConexion  # ya existe en el repo

conn = CConexion.ConexionBaseDeDatos()           # abre la conexión
if conn is None:
    raise RuntimeError("No se pudo conectar a la base de datos")

cursor = conn.cursor(dictionary=True)            # cursor global
