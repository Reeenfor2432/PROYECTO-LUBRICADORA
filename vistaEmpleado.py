import tkinter as tk

#Módulos de tkinter
from tkinter import *
from tkinter import ttk
from vistaPersona import vistaPersona

class vistaEmpleado(vistaPersona):
    def administrarEmpleado(self, base, callback=None):
        groupBox= LabelFrame(base, text="Datos del Empleado", padx=10, pady=10)
        groupBox.pack(pady=10)

        super().interfazBase(groupBox)

        #Campo extra para empleado
        labelRol= Label(groupBox, text= "Identificación del rol:", width=25, font=("arial",12))
        labelRol.grid(row=3, column=0)
        textRol= Entry(groupBox)
        textRol.grid(row=3,column=1)
        labelDom= Label(groupBox, text= "Domicilio:", width=25, font=("arial",12))
        labelDom.grid(row=4, column=0)
        textDom= Entry(groupBox)
        textDom.grid(row=4,column=1)

        Button(groupBox, text= "Añadir", width=15).grid(row=5, column=0)
        Button(groupBox, text= "Modificar", width=15).grid(row=5, column=1)
        Button(groupBox, text= "Eliminar", width=15).grid(row=5, column=2, padx=(40,40))
        
        #Espacio para la tabla
        groupBox= LabelFrame(base,text="Lista de Empleados", padx=5,pady=5,)
        groupBox.pack(pady=10)
        #Crecion de TreeView (widget que permite mostrar tablas)
        tabla= ttk.Treeview(groupBox,columns=("id_empleado","id_rol","nombre", "telefono","domicilio"), show="headings", height=5,)
        tabla.heading("id_empleado", text="Identificacion")
        tabla.heading("id_rol", text="Rol")
        tabla.heading("nombre", text= "Nombre del empleado")
        tabla.heading("telefono", text= "Telefono")
        tabla.heading("domicilio", text= "Domicilio")
        tabla.pack()

        #Regresar al menu
        if callback:
            regresar= Button(base, text="Volver al menú", command=callback).pack(pady=10)

# Falta modificar y mostrar tabla en una misma ventana, ver el video que envie...