import tkinter as tk

#Módulos de tkinter
from tkinter import *

#Clase VistaPersona

class vistaPersona:

    def interfazBase(self, container):
            
        #Id
        labelId= Label(container, text= "Ingrese identificación:", width=25, font=("arial",12)).grid(row=0, column=0)
        textBoxNom= Entry(container)
        textBoxNom.grid(row= 0, column= 1)
        #Nombre
        labelNom= Label(container, text= "Ingrese el nombre:", width=25, font=("arial",12)).grid(row=1, column=0)
        textBoxNom= Entry(container)
        textBoxNom.grid(row= 1, column= 1)
        #Telefono
        labelTel= Label(container, text= "Ingrese número de teléfono:", width=25, font=("arial",12)).grid(row=2, column=0)
        textBoxTel= Entry(container)
        textBoxTel.grid(row= 2, column= 1)
