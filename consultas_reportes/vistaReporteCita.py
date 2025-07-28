import tkinter as tk
from tkinter import ttk
from tkinter import *
from claseUtilitaria import claseUtilitaria
from consultas_reportes.vistaCitasCompletas import vistaCitasCompletas
from consultas_reportes.vistaCitasFrecuentes import vistaCitasFrecuentes
from consultas_reportes.vistaCitasPendiente import vistaCitasPendientes

class vistaReporteCita:
    def __init__(self):
        self.tabla= None
        self.base= None
    def interfazReporteCita(self,base,callbackReporte=None):
        self.base = base
        groupbox= LabelFrame(base, text="Reportes de citas", padx=10, pady=10)
        groupbox.pack(pady=10)

        #Botones para reportes de citas (faltan command)
        btnCitasCompletas= Button(groupbox, text="Mostrar todas las citas", width=50, command= self.motrarCitasCompletas)
        btnCitasCompletas.grid(row=0,column=0)
        btnCitasFrecuente= Button(groupbox, text="Mostrar las citas de los clientes frecuentes", width=50, command= self.mostratCitasFrecuentes)
        btnCitasFrecuente.grid(row=1,column=0)
        btnCitasPendientes= Button(groupbox, text="Mostrar las citas pendientes", width=50, command=self.mostrarCitasPendientes)
        btnCitasPendientes.grid(row=2,column=0)

        #Tabla de citas
        self.tabla= claseUtilitaria.tablaParaCita(base)

        if callbackReporte:
            Button(base,text="Volver a Reportes", command=lambda:callbackReporte(base)).pack(pady=10)
    
    def motrarCitasCompletas(self):
        citastodas= vistaCitasCompletas()
        citastodas.interfazCitasCompletas(self.tabla)

    def mostratCitasFrecuentes(self):
        citasfrec = vistaCitasFrecuentes()
        citasfrec.interfazCitasFrecuentes(self.tabla)

    def mostrarCitasPendientes(self):
        citaspend= vistaCitasPendientes()
        citaspend.interfazCitasPendientes(self.tabla)
