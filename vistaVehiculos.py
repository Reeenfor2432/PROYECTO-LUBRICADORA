import tkinter as tk
from tkinter import *
from tkinter import ttk,messagebox
from Guardado_de_datos.AdminVehiculo import manejarVehiculo

class vistaVehiculo:
    def administrarVehiculo(self,base, callbackMenu=None):
        groupBox= LabelFrame(base, text="Datos del Vehículo", padx=10, pady=10 )
        groupBox.pack(pady=10)

        labelId= Label(groupBox, text= "Placa del vehículo:", width=25, font=("arial",12))
        labelId.grid(row=0, column=0)
        self.textId= Entry(groupBox)
        self.textId.grid(row=0,column=1)

        labelClie= Label(groupBox, text= "ID del cliente:", width=25, font=("arial",12))
        labelClie.grid(row=1, column=0)
        self.textClie= Entry(groupBox)
        self.textClie.grid(row=1,column=1)

        labelMarca= Label(groupBox, text= "Marca:", width=25, font=("arial",12))
        labelMarca.grid(row=2, column=0)
        self.textMarca= Entry(groupBox)
        self.textMarca.grid(row=2,column=1)

        labelColor= Label(groupBox, text= "Color:", width=25, font=("arial",12))
        labelColor.grid(row=3, column=0)
        self.textColor= Entry(groupBox)
        self.textColor.grid(row=3,column=1)

        labelModel= Label(groupBox, text= "Modelo:", width=25, font=("arial",12))
        labelModel.grid(row=4, column=0)
        self.textModel= Entry(groupBox)
        self.textModel.grid(row=4,column=1)

        labelA= Label(groupBox, text= "Año:", width=25, font=("arial",12))
        labelA.grid(row=5, column=0)
        self.textA= Entry(groupBox)
        self.textA.grid(row=5,column=1)
        

        Button(groupBox, text= "Añadir", width=15, command= self.guardarRegistros).grid(row=6, column=0)
        Button(groupBox, text= "Modificar", width=15, command= self.modificarRegistro).grid(row=6, column=1)
        Button(groupBox, text= "Eliminar", width=15, command= self.eliminarRegistro).grid(row=6, column=2, padx=(40,40))
        
        #Espacio para la tabla
        groupBox= LabelFrame(base,text="Lista de Vehículos", padx=5,pady=5,)
        groupBox.pack(pady=10)
        #Crecion de TreeView (widget que permite mostrar tablas)
        self.tabla= ttk.Treeview(groupBox,columns=("placa","cedula","marca","color","modelo","año"), show="headings", height=5,)
        self.tabla.heading("placa", text="Placa")
        self.tabla.column("placa",width=100, anchor="w")
        self.tabla.heading("cedula", text= "ID de Cliente")
        self.tabla.column("cedula",width=100, anchor="w")
        self.tabla.heading("marca", text= "Marca")
        self.tabla.column("marca",width=120, anchor="w")
        self.tabla.heading("color", text= "Color")
        self.tabla.column("color",width=120, anchor="w")
        self.tabla.heading("modelo", text= "Modelo")
        self.tabla.column("modelo",width=120, anchor="w")
        self.tabla.heading("año", text= "Año de fabricación")
        self.tabla.column("año",width=120, anchor="w")
        self.tabla.pack()

        # Vincular el evento de selección de un registro de la tabla
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionarRegistro)

        # Cargar los datos de la base de datos y actualizarlos en la tabla
        self.actualizarVistaTabla()
        
        if callbackMenu:
            regresar= Button(base, text="Volver al menú", command=callbackMenu).pack(pady=10)
        
        # Método para guardar registros en la base de datos
    def guardarRegistros(self):
        try:
            # Obtener los valores de los campos de entrada
            self.obtenerTexto()

            # Llamar a la función para agregar un vehiculo
            manejarVehiculo.IngresarVehiculo(self.placa, self.id_cliente, self.marca, self.color, self.modelo, self.año)
            messagebox.showinfo("INFORMACIÓN", "Los datos fueron ingresados exitosamente")

            # Limpiar los campos de entrada después de guardar
            self.limpiarTexto()

            # Actualizar la vista de la tabla
            self.actualizarVistaTabla()

        except ValueError as error:
            # Si hay un error, se imprime en la consola
            print("Error al ingresar los datos: {}".format(error))

    # Método para actualizar la vista de la tabla de empleados
    def actualizarVistaTabla(self):
        try:
            # Limpiar la tabla antes de cargar los nuevos datos
            self.tabla.delete(*self.tabla.get_children())

            # Obtener los datos de los empleados desde la base de datos
            datos = manejarVehiculo.MostrarVehiculo()

            # Insertar cada fila de datos en la tabla
            for row in datos:
                self.tabla.insert("", "end", values=row)

        except Exception as error:
            # Si hay un error, se imprime en la consola
            print("Error al actualizar tabla: {}".format(error))

    # Método para seleccionar un registro de la tabla y mostrarlo en los campos de entrada
    def seleccionarRegistro(self, event):
        try:
            item = self.tabla.focus()  # Obtener el registro seleccionado
            if item:
                values = self.tabla.item(item)['values']  # Obtener los valores del registro seleccionado
                
                # Insertar los valores seleccionados en los campos de entrada
                self.limpiarTexto()
                self.insertarTexto(values)

                self.placa_vieja= self.textId.get() #Guardar una version de la placa antes de ser modificada (Para Modificar)


        except Exception as error:
            # Si hay un error, se imprime en la consola
            print("Error al seleccionar:", error)

    # Método para modificar un registro existente en la base de datos
    def modificarRegistro(self):
        try:
            # Obtener los valores de los campos de entrada
            self.obtenerTexto()
            # Llamar a la función para modificar los datos del cliente
            manejarVehiculo.ModificarVehiculo(self.placa,self.placa_vieja, self.id_cliente, self.marca, self.color, self.modelo, self.año)
            print(self.placa_vieja)
            print(self.placa)
            messagebox.showinfo("INFORMACIÓN", "Los datos fueron modificados exitosamente")

            # Limpiar los campos de entrada después de modificar
            self.limpiarTexto()

            # Actualizar la vista de la tabla
            self.actualizarVistaTabla()

        except ValueError as error:
            # Si hay un error, se imprime en la consola
            print("Error al modificar los datos: {}".format(error))

    # Método para eliminar un registro de la base de datos
    def eliminarRegistro(self):
        try:
            # Obtener el ID del cliente a eliminar
            placa_a_eliminar = self.textId.get()

            # Llamar a la función para eliminar el cliente
            manejarVehiculo.EliminarVehiculo(placa_a_eliminar)
            messagebox.showinfo("INFORMACIÓN", "Los datos fueron eliminados exitosamente")

            # Limpiar los campos de entrada después de eliminar
            self.limpiarTexto()

            # Actualizar la vista de la tabla
            self.actualizarVistaTabla()

        except ValueError as error:
            # Si hay un error, se imprime en la consola
            print("Error al modificar los datos: {}".format(error))
    
    
    def limpiarTexto(self):
        self.textId.delete(0, END)
        self.textClie.delete(0, END)
        self.textMarca.delete(0, END)
        self.textColor.delete(0, END)
        self.textModel.delete(0, END)
        self.textA.delete(0, END)
    
    def insertarTexto(self,values):
        self.textId.insert(0, values[0])                
        self.textClie.insert(0, f"{int(values[1]):03d}")  # 3 dígitos en formato               
        self.textMarca.insert(0, values[2])               
        self.textColor.insert(0, values[3])
        self.textModel.insert(0, values[4])
        self.textA.insert(0, values[5])
    
    def obtenerTexto(self):
            self.placa = self.textId.get()
            self.id_cliente = self.textClie.get()
            self.marca = self.textMarca.get()
            self.color = self.textColor.get()
            self.modelo= self.textModel.get()
            self.año= self.textA.get()

