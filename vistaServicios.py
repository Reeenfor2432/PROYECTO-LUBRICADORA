import tkinter as tk
from tkinter import *
from tkinter import ttk

class vistaServicio:
    def administrarServicio(self,base, callback=None):
        groupBox= LabelFrame(base, text="Datos del Servicio", padx=10, pady=10 )
        groupBox.pack(pady=20)

        labelId= Label(groupBox, text= "Identificación del servicio:", width=25, font=("arial",12))
        labelId.grid(row=0, column=0)
        textId= Entry(groupBox)
        textId.grid(row=0,column=1)

        labelNom= Label(groupBox, text= "Nombre del servicio:", width=25, font=("arial",12))
        labelNom.grid(row=1, column=0)
        textNom= Entry(groupBox)
        textNom.grid(row=1,column=1)

        labelPrecio= Label(groupBox, text= "Precio unitario:", width=25, font=("arial",12))
        labelPrecio.grid(row=2, column=0)
        textPrecio= Entry(groupBox)
        textPrecio.grid(row=2,column=1)

        Button(groupBox, text= "Añadir", width=15).grid(row=3, column=0)
        Button(groupBox, text= "Modificar", width=15).grid(row=3, column=1)
        Button(groupBox, text= "Eliminar", width=15).grid(row=3, column=2, padx=(40,40))
        
        #Espacio para la tabla
        groupBox= LabelFrame(base,text="Lista de Servicios", padx=5,pady=5,)
        groupBox.pack(pady=10)
        #Crecion de TreeView (widget que permite mostrar tablas)
        tabla= ttk.Treeview(groupBox,columns=("id_servicio","Nombre_servicio","Precio"), show="headings", height=5,)
        tabla.heading("id_servicio", text="Identificacion")
        tabla.heading("Nombre_servicio", text= "Nombre del servicio")
        tabla.heading("Precio", text= "Precio unitario")
        tabla.pack()
        
        if callback:
            regresar= Button(base, text="Volver al menú", command=callback).pack(pady=10)
