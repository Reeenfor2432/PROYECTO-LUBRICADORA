from tkinter import *
from tkinter import ttk, messagebox
from vistaPersona import vistaPersona
from Guardado_de_datos.AgregarClientes import Aggclientes


class vistaCliente(vistaPersona):
    # Método principal para administrar los clientes, con base en una ventana base
    def administrarCliente(self, base, callback=None):
        # Crear un cuadro de grupo (LabelFrame) para mostrar los datos del cliente
        groupBox = LabelFrame(base, text="Datos del Cliente", padx=10, pady=10)
        groupBox.pack(pady=10)

        # Llamar a la interfaz base para crear campos comunes de entrada (heredados de vistaPersona)
        super().interfazBase(groupBox)

        # Crear botones de acción para añadir, modificar y eliminar registros
        Button(groupBox, text="Añadir", width=15, command=self.guardarRegistros).grid(row=4, column=0)
        Button(groupBox, text="Modificar", width=15, command=self.modificarRegistro).grid(row=4, column=1)
        Button(groupBox, text="Eliminar", width=15, command=self.eliminarRegistro).grid(row=4, column=2, padx=(40, 40))

        # Crear un frame para mostrar la tabla de clientes
        tablaFrame = LabelFrame(base, text="Lista de Clientes", padx=5, pady=5)
        tablaFrame.pack(pady=10)

        # Crear una tabla (Treeview) con las columnas ID, cedula, nombre_cliente y telefono
        self.tabla = ttk.Treeview(tablaFrame, columns=("ID","cedula", "nombre_cliente", "telefono"), show="headings", height=5)
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("cedula", text="cedula")
        self.tabla.heading("nombre_cliente", text="Nombre del cliente")
        self.tabla.heading("telefono", text="Teléfono")
        self.tabla.pack()

        # Vincular el evento de selección de un registro de la tabla
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionarRegistro)

        # Cargar los datos de la base de datos y actualizarlos en la tabla
        self.actualizarVistaTabla()

        # Botón para volver al menú principal
        if callback:
            Button(base, text="Volver al menú", command=callback).pack(pady=10)

    # Método para guardar registros en la base de datos
    def guardarRegistros(self):
        try:
            # Obtener los valores de los campos de entrada
            cedula = self.texBoxCe.get()
            nombre = self.texBoxNom.get()
            telefono = self.texBoxTel.get()

            # Llamar a la función para agregar un cliente
            Aggclientes.IngresarClientes(cedula, nombre, telefono)
            messagebox.showinfo("INFORMACIÓN", "Los datos fueron ingresados exitosamente")

            # Limpiar los campos de entrada después de guardar
            self.texBoxCe.delete(0, END)
            self.texBoxNom.delete(0, END)
            self.texBoxTel.delete(0, END)

            # Actualizar la vista de la tabla
            self.actualizarVistaTabla()

        except ValueError as error:
            # Si hay un error, se imprime en la consola
            print("Error al ingresar los datos: {}".format(error))

    # Método para actualizar la vista de la tabla de clientes
    def actualizarVistaTabla(self):
        try:
            # Limpiar la tabla antes de cargar los nuevos datos
            self.tabla.delete(*self.tabla.get_children())

            # Obtener los datos de los clientes desde la base de datos
            datos = Aggclientes.MostrarClientes()

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
                self.texBoxCe.insert(0, f"{int(values[1]):010d}")  # 10 dígitos en formato
                self.texBoxNom.delete(0, END)
                self.texBoxNom.insert(0, values[2])
                
                self.texBoxTel.delete(0, END)
                self.texBoxTel.insert(0, f"{int(values[3]):010d}")  # 10 dígitos en formato
        except Exception as error:
            # Si hay un error, se imprime en la consola
            print("Error al seleccionar:", error)

    # Método para modificar un registro existente en la base de datos
    def modificarRegistro(self):
        try:
            # Obtener los valores de los campos de entrada
            id = self.texBoxId.get()
            cedula = self.texBoxCe.get()
            nombre = self.texBoxNom.get()
            telefono = self.texBoxTel.get()

            # Llamar a la función para modificar los datos del cliente
            Aggclientes.ModificarClientes(id, cedula, nombre, telefono)
            messagebox.showinfo("INFORMACIÓN", "Los datos fueron modificados exitosamente")

            # Limpiar los campos de entrada después de modificar
            self.texBoxId.delete(0, END)
            self.texBoxCe.delete(0, END)
            self.texBoxNom.delete(0, END)
            self.texBoxTel.delete(0, END)

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
            Aggclientes.EliminarClientes(id)
            messagebox.showinfo("INFORMACIÓN", "Los datos fueron eliminados exitosamente")

            # Limpiar los campos de entrada después de eliminar
            self.texBoxId.delete(0, END)
            self.texBoxCe.delete(0, END)
            self.texBoxNom.delete(0, END)
            self.texBoxTel.delete(0, END)

            # Actualizar la vista de la tabla
            self.actualizarVistaTabla()

        except ValueError as error:
            # Si hay un error, se imprime en la consola
            print("Error al modificar los datos: {}".format(error))
