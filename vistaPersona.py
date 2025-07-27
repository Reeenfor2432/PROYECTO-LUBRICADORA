import tkinter as tk

#Módulos de tkinter
from tkinter import *

#Clase VistaPersona

class vistaPersona:

    def interfazBase(self, container):

        #id
        labelid = Label(container, text="ID (solo para eliminar):", width=25, font=("arial",12)).grid(row=0, column=0)
        self.texBoxId = Entry(container)
        self.texBoxId.grid(row=0, column=1)

        #Cedula
        labelCe= Label(container, text= "Ingrese identificación:", width=25, font=("arial",12)).grid(row=1, column=0)
        self.texBoxCe= Entry(container)
        self.texBoxCe.grid(row= 1, column= 1)
        #Nombre
        labelNom= Label(container, text= "Ingrese el nombre:", width=25, font=("arial",12)).grid(row=2, column=0)
        self.texBoxNom= Entry(container)
        self.texBoxNom.grid(row= 2, column= 1)
        #Telefono
        labelTel= Label(container, text= "Ingrese número de teléfono:", width=25, font=("arial",12)).grid(row=3, column=0)
        self.texBoxTel= Entry(container)
        self.texBoxTel.grid(row= 3, column= 1)
