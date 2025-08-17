import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from Guardado_de_datos.Conexion import *

#Métodos utilitarios
class claseUtilitaria:
    @staticmethod
    def limpiarVentana(base):
        for elemento in base.winfo_children():
            elemento.destroy()
    @staticmethod
    def limpiarTabla(tabla):
        for fila in tabla.get_children():
            tabla.delete(fila)

    @staticmethod
    def tablaParaCitaDetallada(base):
        groupbox = LabelFrame(base, text="Lista de Citas - Clientes Frecuentes", padx=5, pady=5)
        groupbox.pack(pady=10)

        # TreeView con las columnas de la vista
        tabla = ttk.Treeview(
        groupbox,
        columns=(
            "id_cita", "id_cliente", "nombre_cliente", "cedula",
            "placa", "marca", "modelo",
            "id_empleado", "nombre_empleado", "telefono_empleado",
            "hora_ingreso", "hora_salida", "estado"),show="headings")

        # Encabezados y configuración de columnas
        tabla.heading("id_cita", text="ID Cita")
        tabla.column("id_cita", width=80, anchor="w")

        tabla.heading("id_cliente", text="ID Cliente")
        tabla.column("id_cliente", width=80, anchor="w")

        tabla.heading("nombre_cliente", text="Nombre Cliente")
        tabla.column("nombre_cliente", width=150, anchor="w")

        tabla.heading("cedula", text="Cédula")
        tabla.column("cedula", width=100, anchor="w")

        tabla.heading("placa", text="Placa Vehículo")
        tabla.column("placa", width=100, anchor="w")


        tabla.heading("id_empleado", text="ID Empleado")
        tabla.column("id_empleado", width=100, anchor="w")

        tabla.heading("nombre_empleado", text="Empleado")
        tabla.column("nombre_empleado", width=150, anchor="w")

        tabla.heading("hora_ingreso", text="Hora Ingreso")
        tabla.column("hora_ingreso", width=120, anchor="w")

        tabla.heading("hora_salida", text="Hora Salida")
        tabla.column("hora_salida", width=120, anchor="w")

        tabla.heading("estado", text="Estado Cita")
        tabla.column("estado", width=80, anchor="w")

        tabla.pack(pady=10)
        return tabla
    
    # ------------------------------------------------------------------
    # Tabla para la vista de Roles
    # ------------------------------------------------------------------
    @staticmethod
    def tablaParaRol(base):
        groupbox= LabelFrame(base, text="Lista de Roles", padx=5, pady=5,)
        groupbox.pack(pady=10)
        """
        Devuelve un Treeview con las 3 columnas de la tabla rol:
        id_rol | nombre_rol | descripcion
        """
        cols = ("id_rol", "nombre_rol", "descripcion")
        tabla = ttk.Treeview(groupbox, columns=cols, show="headings", height=5)

        tabla.heading("id_rol",       text="ID")
        tabla.heading("nombre_rol",  text="Nombre del rol")
        tabla.heading("descripcion", text="Descripción")

        # Ajusta el ancho a tu gusto
        tabla.column("id_rol",       width=60,  anchor="w")
        tabla.column("nombre_rol",   width=150, anchor="w")
        tabla.column("descripcion",  width=350, anchor="w")

        tabla.pack(pady=10)
        return tabla

    # ------------------------------------------------------------------
    # Tabla para la vista de Servicios
    # ------------------------------------------------------------------
    @staticmethod
    def tablaParaServicio(base):
        groupbox= LabelFrame(base, text="Lista de Servicios", padx=5, pady=5,)
        groupbox.pack(pady=10)
        cols = ("id_servicio", "nombre", "precio")

        tabla = ttk.Treeview(
            groupbox, columns=cols, show="headings", height=5
        )

        # Encabezados
        tabla.heading("id_servicio", text="ID")
        tabla.heading("nombre",      text="Nombre del servicio")
        tabla.heading("precio",      text="Precio $")

        # Anchos / alineación
        tabla.column("id_servicio", width=60,  anchor="w")
        tabla.column("nombre",      width=220, anchor="w")
        tabla.column("precio",      width=80,  anchor="w")

        tabla.pack(pady=10)
        return tabla


    @staticmethod
    def eliminarTabla(tabla):
        if tabla is not None:
            tabla.destroy()
    
    @staticmethod
    def limpiarGroupbox(groupB):
        for widget in groupB.winfo_children():
                widget.destroy()
    
    @staticmethod
    def eliminarGroupbox(groupbox):
        if groupbox is not None:
            groupbox.destroy()

    
    #METODOS PARA SQL
    @staticmethod
    def buscarCedulaPorId(id_cliente):
        try:
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()

            sql = "SELECT cedula FROM cliente WHERE id_cliente = %s"
            cursor.execute(sql, (id_cliente,))
            resultado = cursor.fetchone()

            cursor.close()
            conec.close()

            if resultado:
                return resultado[0]  # regresa cedula
            else:
                print("Cliente no encontrado.")
                return None

        except mysql.connector.Error as error:
            print("Error al obtener la cédula del cliente:", error)
            return None
        
    
