import tkinter as tk
from tkinter import *
from tkinter import ttk
from claseUtilitaria import claseUtilitaria
from Guardado_de_datos.Conexion import *


class vistaFactura:
    
    def generarFactura(self, base, callbackMenu):
        self.base= base
        self.descuento = 1
        self.impuesto= 1

        self.seleccionCita(self.base)

        #No sé que puede seguir...

        if callbackMenu:
            regresar= Button(base, text="Volver al menú", command=callbackMenu).pack(pady=10)
    
    
    
    #METODOS PARA FACTURA    
    def seleccionCita(self,base):
        self.groupBox= LabelFrame(base, text="Selección de la cita facturar", padx=10, pady=10 )
        self.groupBox.pack(pady=50)

        labelId= Label(self.groupBox, text= "Ingrese ID de la cita:", width=35, font=("arial",12))
        labelId.grid(row=0, column=0)
        textId= Entry(self.groupBox)
        textId.grid(row=0,column=1)

        #SQL
        id_cita= textId.get()
        # Crear una conexión con la base de datos
        try:
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()  
            sql = "SELECT id_cliente FROM cita WHERE id_cita = %s"
            cursor.execute(sql, (id_cita,))
            resultado = cursor.fetchone()

            # Verificar si se encontró una cita
            if resultado:
                id_cliente= resultado[0]  # Devuelve el id
            else:
                print(cursor.rowcount, "Esta cita no existe")
            cursor.close()
            conec.close()
        except mysql.connector.Error as error:
            print("Error al conectar {}".format(error))

        btnSeleccionar= Button(self.groupBox, text="Seleccionar", width=25, command=lambda: self.ingresarDescuento(id_cliente))
        btnSeleccionar.grid(row=1,column=1)
        
    
    def ingresarDescuento(self, id_cliente):
        # Crear una conexión con la base de datos
        try:
            conec = CConexion.ConexionBaseDeDatos()
            cursor = conec.cursor()  
            sql_cliente = "SELECT id_cliente FROM cliente WHERE id_cliente WHERE id_cliente IN (SELECT id_cliente FROM cita GROUP BY id_cliente HAVING COUNT(*) > 5);"
            cursor.execute(sql_cliente, (id_cliente,))
            resultado = cursor.fetchone()            
            cursor.close()
            conec.close()

        except mysql.connector.Error as error:
            print("Error al conectar {}".format(error))

        if resultado:
            Labeldescuento=Label(self.groupBox, text="El cliente es frecuente ¿Desea aplicar descuento?:",width=60)
            Labeldescuento.pack(pady=10)
            Textdescuento= Entry(self.groupBox)
            Textdescuento.pack(pady=10)
            
            self.descuento=  1 - (float(Textdescuento.get())/100)
        else:
            self.descuento= 1 
        btnIngresar= Button(self.groupBox, text= "Ingresar", width=15, command=lambda: self.ingresarImpuesto())

    def ingresarImpuesto(self):
        Labelimpuesto=Label(self.groupBox, text="Ingrese el impuesto o IVA:",width=60)
        Labelimpuesto.pack(pady=10)
        Textimpuesto= Entry(self.groupBox)
        Textimpuesto.pack(pady=10)
        self.impuesto: 1 + (float(Textimpuesto.get()) /100)
        btnIngresar= Button(self.groupBox, text= "Ingresars", width=15, command=lambda: self.ingresarImpuesto())
        claseUtilitaria.limpiarVentana(self.base)