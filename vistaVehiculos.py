import tkinter as tk
from tkinter import *
from tkinter import ttk

class vistaVehiculo:
    def administrarVehiculo(self,base, callbackMenu=None):
        groupBox= LabelFrame(base, text="Datos del Vehículo", padx=10, pady=10 )
        groupBox.pack(pady=10)

        labelId= Label(groupBox, text= "Placa del vehículo:", width=25, font=("arial",12))
        labelId.grid(row=0, column=0)
        textId= Entry(groupBox)
        textId.grid(row=0,column=1)

        labelClie= Label(groupBox, text= "ID del cliente:", width=25, font=("arial",12))
        labelClie.grid(row=1, column=0)
        textClie= Entry(groupBox)
        textClie.grid(row=1,column=1)

        labelMarca= Label(groupBox, text= "Marca:", width=25, font=("arial",12))
        labelMarca.grid(row=2, column=0)
        textMarca= Entry(groupBox)
        textMarca.grid(row=2,column=1)

        labelColor= Label(groupBox, text= "Color:", width=25, font=("arial",12))
        labelColor.grid(row=3, column=0)
        textColor= Entry(groupBox)
        textColor.grid(row=3,column=1)

        labelModel= Label(groupBox, text= "Modelo:", width=25, font=("arial",12))
        labelModel.grid(row=4, column=0)
        textModel= Entry(groupBox)
        textModel.grid(row=4,column=1)

        labelA= Label(groupBox, text= "Año:", width=25, font=("arial",12))
        labelA.grid(row=5, column=0)
        textA= Entry(groupBox)
        textA.grid(row=5,column=1)
        

        Button(groupBox, text= "Añadir", width=15).grid(row=6, column=0)
        Button(groupBox, text= "Modificar", width=15).grid(row=6, column=1)
        Button(groupBox, text= "Eliminar", width=15).grid(row=6, column=2, padx=(40,40))
        
        #Espacio para la tabla
        groupBox= LabelFrame(base,text="Lista de Vehículos", padx=5,pady=5,)
        groupBox.pack(pady=10)
        #Crecion de TreeView (widget que permite mostrar tablas)
        tabla= ttk.Treeview(groupBox,columns=("placa","cedula","marca","color","modelo","año"), show="headings", height=5,)
        tabla.heading("placa", text="Placa")
        tabla.column("placa",width=100, anchor="w")
        tabla.heading("cedula", text= "ID de Cliente")
        tabla.column("cedula",width=100, anchor="w")
        tabla.heading("marca", text= "Marca")
        tabla.column("marca",width=120, anchor="w")
        tabla.heading("color", text= "Color")
        tabla.column("color",width=120, anchor="w")
        tabla.heading("modelo", text= "Modelo")
        tabla.column("modelo",width=120, anchor="w")
        tabla.heading("año", text= "Año de fabricación")
        tabla.column("año",width=120, anchor="w")
        tabla.pack()
        
        if callbackMenu:
            regresar= Button(base, text="Volver al menú", command=callbackMenu).pack(pady=10)
