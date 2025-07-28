import tkinter as tk
from tkinter import *
from tkinter import ttk
from consultas_reportes.vistaReporteCita import vistaReporteCita
from consultas_reportes.vistaReporteProductosStock import vistaReporteProductosStock
from consultas_reportes.vistaReporteIngresoPorServ import vistaReporteIngreso
from claseUtilitaria import claseUtilitaria

class vistaReporte:
   
    def interfazReporte(self,base,callbackMenu=None):
        self.base=base
        self.callbackMenu= callbackMenu

        claseUtilitaria.limpiarVentana(base)
        groupbox= LabelFrame(base, text="Reportes", padx=10, pady=10)
        groupbox.pack(pady=10)

        #Botones para reportes (faltan command)
        btnCitas= Button(groupbox, text="Mostrar reportes de citas", width=70, command= self.mostrarVistaReporteCita)
        btnCitas.grid(row=0,column=0)
        btnStock=Button(groupbox, text="Mostrar los productos con stock menor a 5", width=70, command=self.mostrarVistaReporteStock)
        btnStock.grid(row=1,column=0)
        btnIngreso= Button(groupbox, text="Mostrar el ingreso total por servicio", width=70, command=self.mostrarVistaReporteIngreso)
        btnIngreso.grid(row=2,column=0)

        if callbackMenu:
            Button(base,text="Volver al menú", command= callbackMenu).pack(pady=10)

    #Metodo para mostrar la vista Citas en Reporte (para gerente)
    def mostrarVistaReporteCita(self):
        claseUtilitaria.limpiarVentana(self.base)
        vistacitas= vistaReporteCita()
        vistacitas.interfazReporteCita(self.base, lambda base: self.interfazReporte(base, self.callbackMenu))
    
    def mostrarVistaReporteStock(self):
        vistaprod= vistaReporteProductosStock()
        vistaprod.interfazReporteStock(self.base)

    def mostrarVistaReporteIngreso(self):
        vistaingreso= vistaReporteIngreso()
        vistaingreso.interfazReporteIngreso(self.base)
        