import tkinter as tk

#Módulos de tkinter
from tkinter import *
from vistaPersona import vistaPersona

class vistaEmpleado(vistaPersona):
    def administrarEmpleado(self, base, callback=None):
        groupBox= LabelFrame(base, text="Datos del Empleado", padx=10, pady=10)
        groupBox.pack(pady=20)

        super().interfazBase(groupBox)

        #Campo extra para empleado
        labelRol= Label(groupBox, text= "Id del rol:", width=25, font=("arial",12))
        labelRol.grid(row=3, column=0)
        textRol= Entry(groupBox)
        textRol.grid(row=3,column=1)
        labelDom= Label(groupBox, text= "Domicilio:", width=25, font=("arial",12))
        labelDom.grid(row=4, column=0)
        textDom= Entry(groupBox)
        textDom.grid(row=4,column=1)

        if callback:
            regresar= Button(base, text="Volver al menú", command=callback).pack(pady=10)