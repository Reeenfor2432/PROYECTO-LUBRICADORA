import tkinter as tk
from tkinter import *
from vistaCliente import vistaCliente
from vistaEmpleado import vistaEmpleado
from vistaServicios import vistaServicio
from vistaInventario import vistaInventario

class menu:
    #Inicializa el menu y lo muestra
    def __init__(self, base):
        self.base = base
        self.mostrarMenu()
    #Borra antes de cambiar de ventana
    def limpiarVentana(self):
        for elemento in self.base.winfo_children():
            elemento.destroy()
    #Metodo para mostrar el menu principal
    def mostrarMenu(self):
        self.limpiarVentana()

        labelSelect= Label(self.base, text= "Seleccione una opción", font=("Arial", 14))
        labelSelect.pack(pady=20)

        btnCliente= Button(self.base, text="Administrar clientes", width=20, command=self.mostrarCliente)
        btnCliente.pack(pady=10)
        btnEmpleado= Button(self.base, text="Administrar empleados", width=20, command=self.mostrarEmpleado)
        btnEmpleado.pack(pady=10)
        btnServicio= Button(self.base, text="Administrar servicios", width=20, command=self.mostrarServicio)
        btnServicio.pack(pady=10)
        btnInventario= Button(self.base, text="Administrar Inventario", width=20, command=self.mostrarInventario)
        btnInventario.pack(pady=10)
    #Falta....

    #Metodo para mostrar la vista cliente (para gerente)
    def mostrarCliente(self):
        self.limpiarVentana()
        vistacliente= vistaCliente()
        vistacliente.administrarCliente(self.base, self.mostrarMenu) #Aquí actua el callback

    #Metodo para mostrar la vista empleado (para gerente)
    def mostrarEmpleado(self):
        self.limpiarVentana()
        vistaempleado= vistaEmpleado()
        vistaempleado.administrarEmpleado(self.base, self.mostrarMenu)
    
    def mostrarServicio(self):
        self.limpiarVentana()
        vistaservicio= vistaServicio()
        vistaservicio.administrarServicio(self.base, self.mostrarMenu)
    
    def mostrarInventario(self):
        self.limpiarVentana()
        vistainv = vistaInventario()
        vistainv.administrarInventario(self.base, self.mostrarMenu)

