import tkinter as tk

#Módulos de tkinter
from tkinter import *
from tkinter import ttk
from vistaPersona import vistaPersona

class vistaCliente(vistaPersona):

    def administrarCliente(self, base, callback=None):
        groupBox= LabelFrame(base, text="Datos del Cliente", padx=10, pady=10)
        groupBox.pack(pady=10)
        #Llama la interfaz base
        super().interfazBase(groupBox)

        #Campo extra para empleado
        labelFrec= Label(groupBox, text= "¿Frecuente? (Si=1 | No= 0)", width=25, font=("arial",12))
        labelFrec.grid(row=3, column=0)
        textFrec= Entry(groupBox)
        textFrec.grid(row=3,column=1)

        Button(groupBox, text= "Añadir", width=15).grid(row=4, column=0)
        Button(groupBox, text= "Modificar", width=15).grid(row=4, column=1)
        Button(groupBox, text= "Eliminar", width=15).grid(row=4, column=2, padx=(40,40))
        
        #Espacio para la tabla
        groupBox= LabelFrame(base,text="Lista de Clientes", padx=5,pady=5,)
        groupBox.pack(pady=10)
        #Crecion de TreeView (widget que permite mostrar tablas)
        tabla= ttk.Treeview(groupBox,columns=("cedula","nombre_cliente","telefono", "frecuente"), show="headings", height=5,)
        tabla.heading("cedula", text="Identificacion")
        tabla.heading("nombre_cliente", text= "Nombre del cliente")
        tabla.heading("telefono", text= "Telefono")
        tabla.heading("frecuente", text= "¿Es frecuente?")
        tabla.pack()
        
        #Regresar al menu
        if callback:
            regresar= Button(base, text="Volver al menú", command=callback).pack(pady=10)
# Falta modificar y mostrar tabla en una misma ventana, ver el video que envie...