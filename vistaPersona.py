import tkinter as tk

# Módulos de tkinter
from tkinter import *

# Clase VistaPersona
class vistaPersona:

    # Método para crear la interfaz base de los campos de entrada
    def interfazBase(self, container):
        # Crear un campo para el ID (usado solo para eliminar registros)
        labelid = Label(container, text="ID (solo para eliminar):", width=25, font=("arial", 12)).grid(row=0, column=0)
        self.texBoxId = Entry(container)  # Campo de entrada para ID
        self.texBoxId.grid(row=0, column=1)  # Ubicación en la interfaz gráfica

        # Crear un campo para la cédula de identidad
        labelCe = Label(container, text="Ingrese identificación:", width=25, font=("arial", 12)).grid(row=1, column=0)
        self.texBoxCe = Entry(container)  # Campo de entrada para cédula
        self.texBoxCe.grid(row=1, column=1)  # Ubicación en la interfaz gráfica

        # Crear un campo para el nombre del cliente
        labelNom = Label(container, text="Ingrese el nombre:", width=25, font=("arial", 12)).grid(row=2, column=0)
        self.texBoxNom = Entry(container)  # Campo de entrada para el nombre
        self.texBoxNom.grid(row=2, column=1)  # Ubicación en la interfaz gráfica

        # Crear un campo para el número de teléfono
        labelTel = Label(container, text="Ingrese número de teléfono:", width=25, font=("arial", 12)).grid(row=3, column=0)
        self.texBoxTel = Entry(container)  # Campo de entrada para teléfono
        self.texBoxTel.grid(row=3, column=1)  # Ubicación en la interfaz gráfica
