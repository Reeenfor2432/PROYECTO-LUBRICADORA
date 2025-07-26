import tkinter as tk
from tkinter import *
from vistaCliente import vistaCliente
from vistaEmpleado import vistaEmpleado
from vistaServicios import vistaServicio
from vistaInventario import vistaInventario
from vistaRol import vistaRol
from vistaReporte import vistaReporte
from claseUtilitaria import claseUtilitaria

class menu:
    #Inicializa el menu y lo muestra
    def __init__(self, base):
        self.base = base
        self.mostrarMenu()

    #Metodo para mostrar el menu principal
    def mostrarMenu(self):
        claseUtilitaria.limpiarVentana(self.base)

        labelSelect= Label(self.base, text= "Seleccione una opción", font=("Arial", 14))
        labelSelect.pack(pady=20)

        btnCliente= Button(self.base, text="Administrar clientes", width=20, command=self.mostrarCliente)
        btnCliente.pack(pady=10)
        btnEmpleado= Button(self.base, text="Administrar empleados", width=20, command=self.mostrarEmpleado)
        btnEmpleado.pack(pady=10)
        btnServicio= Button(self.base, text="Administrar servicios", width=20, command=self.mostrarServicio)
        btnServicio.pack(pady=10)
        btnInventario= Button(self.base, text="Administrar inventario", width=20, command=self.mostrarInventario)
        btnInventario.pack(pady=10)
        btnRol= Button(self.base, text="Administrar roles", width=20, command=self.mostrarRol)
        btnRol.pack(pady=10)
        btnReportes= Button(self.base, text="Generar Reportes", width=20, command=self.mostrarReportes)
        btnReportes.pack(pady=10)
    #Falta....

    #Metodo para mostrar la vista cliente (para gerente)
    def mostrarCliente(self):
        claseUtilitaria.limpiarVentana(self.base)        
        vistacliente= vistaCliente()
        vistacliente.administrarCliente(self.base, self.mostrarMenu) #Aquí actua el callback

    #Metodo para mostrar la vista empleado (para gerente)
    def mostrarEmpleado(self):
        claseUtilitaria.limpiarVentana(self.base)
        vistaempleado= vistaEmpleado()
        vistaempleado.administrarEmpleado(self.base, self.mostrarMenu)
    
    def mostrarServicio(self):
        claseUtilitaria.limpiarVentana(self.base)
        vistaservicio= vistaServicio()
        vistaservicio.administrarServicio(self.base, self.mostrarMenu)
    
    def mostrarInventario(self):
        claseUtilitaria.limpiarVentana(self.base)
        vistainv = vistaInventario()
        vistainv.administrarInventario(self.base, self.mostrarMenu)
    
    def mostrarRol(self):
        claseUtilitaria.limpiarVentana(self.base)
        vistarol= vistaRol()
        vistarol.administrarRol(self.base, self.mostrarMenu)

    def mostrarReportes(self):
        claseUtilitaria.limpiarVentana(self.base)
        vistareporte= vistaReporte()
        vistareporte.interfazReporte(self.base, self.mostrarMenu)

