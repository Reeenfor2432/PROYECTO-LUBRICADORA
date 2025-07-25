import tkinter as tk
from tkinter import ttk
from tkinter import *
from claseUtilitaria import claseUtilitaria
from consultas_reportes.vistaCitasCompletas import vistaCitasCompletas

class vistaReporteCita:
    def __init__(self):
        self.tabla= None
    
    def interfazReporteCita(self,base,callbackReporte=None):
        groupbox= LabelFrame(base, text="Reportes de citas", padx=10, pady=10)
        groupbox.pack(pady=10)

        self.tabla= None

        #Botones para reportes de citas (faltan command)
        btnCitasCompletas= Button(groupbox, text="Mostrar todas las citas", width=50, command= self.motrarCitasCompletas)
        btnCitasCompletas.grid(row=0,column=0)
        btnCitasFrecuente= Button(groupbox, text="Mostrar las citas de los clientes frecuentes", width=50)
        btnCitasFrecuente.grid(row=1,column=0)
        btnCitasPendientes= Button(groupbox, text="Mostrar las citas pendientes", width=50)
        btnCitasPendientes.grid(row=2,column=0)

        #Tabla de citas
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

        if callbackReporte:
            Button(base,text="Volver a Reportes", command=lambda:callbackReporte(base)).pack(pady=10)
    
    def motrarCitasCompletas(self):
        claseUtilitaria.limpiarTabla(self.tabla)
        citastodas= vistaCitasCompletas()
        citastodas.mostrarCitasCompletas(self.vistaReporteCitas)