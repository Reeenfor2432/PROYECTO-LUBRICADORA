import tkinter as tk

#Módulos de tkinter
from tkinter import *
from tkinter import ttk, messagebox
from vistaPersona import vistaPersona
from Guardado_de_datos.AdminEmpleados import manejarEmpleado

class vistaEmpleado(vistaPersona):
    def administrarEmpleado(self, base, callback=None):
        groupBox= LabelFrame(base, text="Datos del Empleado", padx=10, pady=10)
        groupBox.pack(pady=10)

        super().interfazBase(groupBox)

        #Campo extra para empleado
        labelDom= Label(groupBox, text= "Domicilio:", width=25, font=("arial",12))
        labelDom.grid(row=4, column=0)
        self.textDom= Entry(groupBox)
        self.textDom.grid(row=4,column=1)

        Button(groupBox, text= "Añadir", width=15, command= self.guardarRegistros).grid(row=5, column=0)
        Button(groupBox, text= "Modificar", width=15, command= self.modificarRegistro).grid(row=5, column=1)
        Button(groupBox, text= "Eliminar", width=15, command= self.eliminarRegistro).grid(row=5, column=2, padx=(40,40))
        
        #Espacio para la tabla
        groupBox= LabelFrame(base,text="Lista de Empleados", padx=5,pady=5,)
        groupBox.pack(pady=10)
        #Crecion de TreeView (widget que permite mostrar tablas)
        self.tabla= ttk.Treeview(groupBox,columns=("id_empleado","id_rol","nombre", "telefono","domicilio"), show="headings", height=5,)
        self.tabla.heading("id_empleado", text="Identificacion")
        self.tabla.heading("id_rol", text="Rol")
        self.tabla.heading("nombre", text= "Nombre del empleado")
        self.tabla.heading("telefono", text= "Telefono")
        self.tabla.heading("domicilio", text= "Domicilio")
        self.tabla.pack()

        # Vincular el evento de selección de un registro de la tabla
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionarRegistro)

        # Cargar los datos de la base de datos y actualizarlos en la tabla
        self.actualizarVistaTabla()


        #Regresar al menu
        if callback:
            regresar= Button(base, text="Volver al menú", command=callback).pack(pady=10)

# Método para guardar registros en la base de datos
    def guardarRegistros(self):
        try:
            # Obtener los valores de los campos de entrada
            id_rol = self.texBoxCe.get()
            nombre = self.texBoxNom.get()
            telefono = self.texBoxTel.get()
            domicilio = self.textDom.get()

            # Llamar a la función para agregar un empleado
            manejarEmpleado.IngresarEmpleados(id_rol, nombre, telefono, domicilio)
            messagebox.showinfo("INFORMACIÓN", "Los datos fueron ingresados exitosamente")

            # Limpiar los campos de entrada después de guardar
            self.texBoxCe.delete(0, END)
            self.texBoxNom.delete(0, END)
            self.texBoxTel.delete(0, END)
            self.textDom.delete(0, END)

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
            datos = manejarEmpleado.MostrarEmpleado()

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
                self.texBoxId.delete(0, END)
                self.texBoxId.insert(0, values[0])
                
                self.texBoxCe.delete(0, END)
                self.texBoxCe.insert(0, f"{int(values[1]):03d}")  # 10 dígitos en formato
                self.texBoxNom.delete(0, END)
                self.texBoxNom.insert(0, values[2])
                
                self.texBoxTel.delete(0, END)
                self.texBoxTel.insert(0, f"{int(values[3]):010d}")  # 10 dígitos en formato

                self.textDom.delete(0, END)
                self.textDom.insert(0, values[4])
                
        except Exception as error:
            # Si hay un error, se imprime en la consola
            print("Error al seleccionar:", error)

    # Método para modificar un registro existente en la base de datos
    def modificarRegistro(self):
        try:
            # Obtener los valores de los campos de entrada
            id = self.texBoxId.get()
            id_rol = self.texBoxCe.get()
            nombre = self.texBoxNom.get()
            telefono = self.texBoxTel.get()
            domicilio= self.textDom.get()

            # Llamar a la función para modificar los datos del cliente
            manejarEmpleado.ModificarEmpleados(id, id_rol, nombre, telefono, domicilio)
            messagebox.showinfo("INFORMACIÓN", "Los datos fueron modificados exitosamente")

            # Limpiar los campos de entrada después de modificar
            self.texBoxId.delete(0, END)
            self.texBoxCe.delete(0, END)
            self.texBoxNom.delete(0, END)
            self.texBoxTel.delete(0, END)
            self.textDom.delete(0, END)

            # Actualizar la vista de la tabla
            self.actualizarVistaTabla()

        except ValueError as error:
            # Si hay un error, se imprime en la consola
            print("Error al modificar los datos: {}".format(error))

    # Método para eliminar un registro de la base de datos
    def eliminarRegistro(self):
        try:
            # Obtener el ID del cliente a eliminar
            id = self.texBoxId.get()

            # Llamar a la función para eliminar el cliente
            manejarEmpleado.EliminarEmpleados(id)
            messagebox.showinfo("INFORMACIÓN", "Los datos fueron eliminados exitosamente")

            # Limpiar los campos de entrada después de eliminar
            self.texBoxId.delete(0, END)
            self.texBoxCe.delete(0, END)
            self.texBoxNom.delete(0, END)
            self.texBoxTel.delete(0, END)
            self.textDom.delete(0, END)

            # Actualizar la vista de la tabla
            self.actualizarVistaTabla()

        except ValueError as error:
            # Si hay un error, se imprime en la consola
            print("Error al modificar los datos: {}".format(error))
