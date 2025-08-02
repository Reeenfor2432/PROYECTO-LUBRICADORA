import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

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
    def tablaParaCita(base):
        groupbox= LabelFrame(base, text="Lista de Citas", padx=5, pady=5,)
        groupbox.pack(pady=10)

        tabla= ttk.Treeview(groupbox, columns=("id_cita","cedula","placa","id_empleado","hora_ingreso","hora_salida","estado"),show="headings")
        tabla.heading("id_cita", text="Identificacion")
        tabla.column("id_cita",width=100, anchor="w")
        tabla.heading("cedula", text= "Cedula del cliente")
        tabla.column("cedula",width=120, anchor="w")
        tabla.heading("placa", text= "Placa del vehículo")
        tabla.column("placa",width=120, anchor="w")
        tabla.heading("id_empleado", text="ID del empleado")
        tabla.column("id_empleado",width=120, anchor="w")
        tabla.heading("hora_ingreso", text= "Hora de ingreso")
        tabla.column("hora_ingreso",width=120, anchor="w")
        tabla.heading("hora_salida", text= "Hora de salida")
        tabla.column("hora_salida",width=120, anchor="w")
        tabla.heading("estado", text= "Estado de la cita")
        tabla.column("estado",width=100, anchor="w")
        tabla.pack()
        return tabla
    
    @staticmethod
    def seleccionCita(base):
        groupBox= LabelFrame(base, text="Selección de la cita facturar", padx=10, pady=10 )
        groupBox.pack(pady=50)

        labelId= Label(groupBox, text= "Ingrese ID de la cita:", width=35, font=("arial",12))
        labelId.grid(row=0, column=0)
        textId= Entry(groupBox)
        textId.grid(row=0,column=1)

        btnSeleccionar= Button(groupBox, text="Seleccionar", width=25, command=lambda: claseUtilitaria.aplicarDescuento(groupBox,textId))
        btnSeleccionar.grid(row=1,column=1)
        return textId

    @staticmethod
    def aplicarDescuento(groupBoxT, strFrecuente):
        respuesta= ""
        #SQL....
        if int(strFrecuente.get())== 1:
            Labeldescuento=Label(groupBoxT, text="El cliente es frecuente ¿Desea aplicar descuento?:",width=60)
            Labeldescuento.pack(pady=10)
            Textdescuento= Entry(groupBoxT)
            Textdescuento.pack(pady=10)
            respuesta= Textdescuento
        else:
            respuesta= "Ninguno"  
        btnIngresar= Button(groupBoxT, text= "Ingresar", width=15)
        return respuesta
    
    @staticmethod
    def actualizarVistaTabla(tabla,funcionAgregar):
        try:
            tabla.delete(*tabla.get_children())  # limpiar tabla

            datos = funcionAgregar
            for row in datos:
                tabla.insert("", "end", values=row)

        except Exception as error:
            print("Error al actualizar tabla: {}".format(error))

    @staticmethod
    def eliminarTabla(tabla):
        if tabla is not None:
            tabla.destroy()
    
    @staticmethod
    def eliminarGroupbox(groupbox):
        if groupbox is not None:
            groupbox.destroy()