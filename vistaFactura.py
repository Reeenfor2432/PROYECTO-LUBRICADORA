import tkinter as tk
from tkinter import *
from tkinter import ttk
from claseUtilitaria import claseUtilitaria
class vistaFactura:
    
    def generarFactura(self, base, callbackMenu):
        self.base=base
        id_cita= claseUtilitaria.seleccionCita(self.base)

        #SQL...

        #Labels y Entrys

        if callbackMenu:
            regresar= Button(base, text="Volver al menú", command=callbackMenu).pack(pady=10)
        