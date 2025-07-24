import tkinter as tk

#Módulos de tkinter
from tkinter import *
from vistaPersona import vistaPersona

class vistaCliente(vistaPersona):

    def administrarCliente(self, base, callback=None):
        groupBox= LabelFrame(base, text="Datos del Cliente", padx=10, pady=10)
        groupBox.pack(pady=20)
        #Llama la interfaz base
        super().interfazBase(groupBox)

        #Campo extra para empleado
        labelFrec= Label(groupBox, text= "¿Frecuente? (Si=1 | No= 0)", width=25, font=("arial",12))
        labelFrec.grid(row=3, column=0)
        textFrec= Entry(groupBox)
        textFrec.grid(row=3,column=1)

        #Regresar al menu
        if callback:
            regresar= Button(base, text="Volver al menú", command=callback).pack(pady=10)
# Falta modificar y mostrar tabla en una misma ventana, ver el video que envie...