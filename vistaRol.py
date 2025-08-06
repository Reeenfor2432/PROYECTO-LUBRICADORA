import tkinter as tk
from tkinter import *
from tkinter import ttk

from db import conn, cursor

class vistaRol:
    def administrarRol(self,base,callback=None):
        groupBox= LabelFrame(base, text="Datos del Rol", padx=10, pady=10 )
        groupBox.pack(pady=10)

        labelId= Label(groupBox, text= "Identificación del rol:", width=25, font=("arial",12))
        labelId.grid(row=0, column=0)
        textId= Entry(groupBox)
        textId.grid(row=0,column=1)

        labelNom= Label(groupBox, text= "Nombre del rol:", width=25, font=("arial",12))
        labelNom.grid(row=1, column=0)
        textNom= Entry(groupBox)
        textNom.grid(row=1,column=1)

        labelDesc= Label(groupBox, text= "Descripcion:", width=25, font=("arial",12))
        labelDesc.grid(row=2, column=0)
        textDesc= Entry(groupBox)
        textDesc.grid(row=2,column=1)

        Button(groupBox, text= "Añadir", width=15).grid(row=4, column=0)
        Button(groupBox, text= "Modificar", width=15).grid(row=4, column=1)
        Button(groupBox, text= "Eliminar", width=15).grid(row=4, column=2, padx=(40,40))
        
        #Espacio para la tabla
        groupBox= LabelFrame(base,text="Lista de Roles", padx=5,pady=5,)
        groupBox.pack(pady=10)
        #Crecion de TreeView (widget que permite mostrar tablas)
        tabla= ttk.Treeview(groupBox,columns=("id_rol","nombre_rol","descripcion"), show="headings", height=5,)
        tabla.heading("id_rol", text="Identificacion")
        tabla.heading("nombre_rol", text= "Nombre del rol")
        tabla.heading("descripcion", text= "Descripción del rol")
        tabla.pack()

        if callback:
            regresar= Button(base, text="Volver al menú", command=callback).pack(pady=10)
