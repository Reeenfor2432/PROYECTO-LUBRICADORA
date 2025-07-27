from tkinter import *
from tkinter import ttk, messagebox
from vistaPersona import vistaPersona
from Guardado_de_datos.AgregarClientes import Aggclientes


class vistaCliente(vistaPersona):

    def administrarCliente(self, base, callback=None):
        groupBox = LabelFrame(base, text="Datos del Cliente", padx=10, pady=10)
        groupBox.pack(pady=10)

        # Crear los campos de entrada desde vistaPersona
        super().interfazBase(groupBox)

        # Botones de acción
        Button(groupBox, text="Añadir", width=15, command=self.guardarRegistros).grid(row=4, column=0)
        Button(groupBox, text="Modificar", width=15).grid(row=4, column=1)
        Button(groupBox, text="Eliminar", width=15).grid(row=4, column=2, padx=(40, 40))

        # Crear tabla (TreeView)
        tablaFrame = LabelFrame(base, text="Lista de Clientes", padx=5, pady=5)
        tablaFrame.pack(pady=10)

        self.tabla = ttk.Treeview(tablaFrame, columns=("cedula", "nombre_cliente", "telefono"), show="headings", height=5)
        self.tabla.heading("cedula", text="cedula")
        self.tabla.heading("nombre_cliente", text="Nombre del cliente")
        self.tabla.heading("telefono", text="Teléfono")
        self.tabla.pack()

        # Evento al seleccionar un registro
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionarRegistro)

        # Cargar los datos en la tabla
        self.actualizarVistaTabla()

        # Botón para volver al menú
        if callback:
            Button(base, text="Volver al menú", command=callback).pack(pady=10)

    def guardarRegistros(self):
        try:
            cedula = self.texBoxCe.get()
            nombre = self.texBoxNom.get()
            telefono = self.texBoxTel.get()

            Aggclientes.IngresarClientes(cedula, nombre, telefono)
            messagebox.showinfo("INFORMACIÓN", "Los datos fueron ingresados exitosamente")

            # Limpiar campos
            self.texBoxCe.delete(0, END)
            self.texBoxNom.delete(0, END)
            self.texBoxTel.delete(0, END)

            # Actualizar tabla
            self.actualizarVistaTabla()

        except ValueError as error:
            print("Error al ingresar los datos: {}".format(error))

    def actualizarVistaTabla(self):
        try:
            self.tabla.delete(*self.tabla.get_children())  # limpiar tabla

            datos = Aggclientes.MostrarClientes()
            for row in datos:
                self.tabla.insert("", "end", values=row)

        except Exception as error:
            print("Error al actualizar tabla: {}".format(error))

    def seleccionarRegistro(self, event):
        try:
            itemSeleccionado = self.tabla.focus()

            if itemSeleccionado:
                values = self.tabla.item(itemSeleccionado)['values']

                self.texBoxCe.delete(0, END)
                self.texBoxCe.insert(0, values[0])

                self.texBoxNom.delete(0, END)
                self.texBoxNom.insert(0, values[1])

                self.texBoxTel.delete(0, END)
                self.texBoxTel.insert(0, values[2])
        except Exception as error:
            print("Error al seleccionar registro: {}".format(error))

        

