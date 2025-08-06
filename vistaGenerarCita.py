import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from claseUtilitaria import claseUtilitaria

from db import conn, cursor

class vistaGenerarCita:
    def generarCita(self,base,callbackMenu):
        groupBoxdatos= LabelFrame(base, text= "Datos de la Cita", padx=10, pady=10)
        groupBoxdatos.pack(pady=50)

        labelId= Label(groupBoxdatos, text= "Identificación de cita (Solo en ELIMINAR):", width=35, font=("arial",12))
        labelId.grid(row=0, column=0)
        textId= Entry(groupBoxdatos)
        textId.grid(row=0,column=1)

        labelNom= Label(groupBoxdatos, text="Identificación de cliente:", width=35, font=("arial",12))
        labelNom.grid(row=1, column=0)
        textNom= Entry(groupBoxdatos)
        textNom.grid(row=1,column=1)

        labelP= Label(groupBoxdatos, text= "Placa de vehiculo a registrar:", width=35, font=("arial",12))
        labelP.grid(row=2, column=0)
        textP= Entry(groupBoxdatos)
        textP.grid(row=2,column=1)

        labelEmp= Label(groupBoxdatos, text= "Identificación de empleado a asignar:", width=35, font=("arial",12))
        labelEmp.grid(row=3, column=0)
        textEmp= Entry(groupBoxdatos)
        textEmp.grid(row=3,column=1)

        labeling= Label(groupBoxdatos, text= "Hora de ingreso (YYYY-MM-DD HH:MM:SS):", width=35, font=("arial",12))
        labeling.grid(row=4, column=0)
        texting= Entry(groupBoxdatos)
        texting.grid(row=4,column=1)

        labelsal= Label(groupBoxdatos, text= "Hora de salida (YYYY-MM-DD HH:MM:SS):", width=35, font=("arial",12))
        labelsal.grid(row=5, column=0)
        textsal= Entry(groupBoxdatos)
        textsal.grid(row=5,column=1)

        labelEst= Label(groupBoxdatos, text= "Estado(Opcional): ", width=25, font=("arial",12))
        labelEst.grid(row=6, column=0)
        textEst= Entry(groupBoxdatos)
        textEst.grid(row=6,column=1)

        #Tabla para mostrar las citas
        self.tabla= claseUtilitaria.tablaParaCita(base)

        # Vincular el evento de selección de un registro de la tabla
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionarRegistro)

        # Cargar los datos de la base de datos y actualizarlos en la tabla
        self.actualizarVistaTabla()

        Button(groupBoxdatos, text= "Generar", width=15).grid(row=7, column=0)
        Button(groupBoxdatos, text= "Modificar", width=15).grid(row=7, column=1)
        Button(groupBoxdatos, text= "Eliminar", width=15).grid(row=7, column=2, padx=(40,40))

        if callbackMenu:
            regresar= Button(base, text="Volver al menú", command=callbackMenu).pack(pady=10)
        
        #Metodos para los botones generar, modificar, eliminar... (Copiar y pegar de otras vistas)
