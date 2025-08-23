import tkinter as tk
from tkinter import *
from tkinter import ttk,messagebox
from Guardado_de_datos.AdminProducto import manejarProducto

class vistaInventario:
    def administrarInventario(self,base, callback=None):
        groupBox= LabelFrame(base, text="Datos del Producto", padx=10, pady=10 )
        groupBox.pack(pady=10)

        labelId= Label(groupBox, text= "Identificación del producto:", width=25, font=("arial",12))
        labelId.grid(row=0, column=0)
        self.textId= Entry(groupBox)
        self.textId.grid(row=0,column=1)

        labelNom= Label(groupBox, text= "Nombre del producto:", width=25, font=("arial",12))
        labelNom.grid(row=1, column=0)
        self.textNom= Entry(groupBox)
        self.textNom.grid(row=1,column=1)

        labelD= Label(groupBox, text= "Descripción", width=25, font=("arial",12))
        labelD.grid(row=2, column=0)
        self.textD= Entry(groupBox)
        self.textD.grid(row=2,column=1)

        labelPrecio= Label(groupBox, text= "Precio unitario", width=25, font=("arial",12))
        labelPrecio.grid(row=3, column=0)
        self.textPrecio= Entry(groupBox)
        self.textPrecio.grid(row=3,column=1)

        labelSt= Label(groupBox, text= "Stock actual:", width=25, font=("arial",12))
        labelSt.grid(row=4, column=0)
        self.textSt= Entry(groupBox)
        self.textSt.grid(row=4,column=1)

        labelMarca= Label(groupBox, text= "Nombre de la marca", width=25, font=("arial",12))
        labelMarca.grid(row=5, column=0)
        self.textMarca= Entry(groupBox)
        self.textMarca.grid(row=5,column=1)

        labelCat= Label(groupBox, text= "Nombre de la categoría", width=25, font=("arial",12))
        labelCat.grid(row=6, column=0)
        self.textCat= Entry(groupBox)
        self.textCat.grid(row=6,column=1)

        Button(groupBox, text= "Añadir", width=15, command=self.guardarRegistros).grid(row=7, column=0)
        Button(groupBox, text= "Modificar", width=15, command=self.modificarRegistro).grid(row=7, column=1)
        Button(groupBox, text= "Eliminar", width=15, command= self.eliminarRegistro).grid(row=7, column=2, padx=(40,40))
        
        #Espacio para la tabla
        groupBox= LabelFrame(base,text="Lista de Productos", padx=5,pady=5,)
        groupBox.pack(pady=10)
        #Crecion de TreeView (widget que permite mostrar tablas)
        self.tabla= ttk.Treeview(groupBox,columns=("id_producto","nombre_producto","descripcion", "precio_unitario", "stock", "id_marca", "id_categoria"), show="headings", height=5,)
        self.tabla.heading("id_producto", text="Identificacion")
        self.tabla.column("id_producto",width=100, anchor="w")
        self.tabla.heading("nombre_producto", text= "Nombre del producto")
        self.tabla.column("nombre_producto",width=130, anchor="w")
        self.tabla.heading("descripcion", text= "Descripcion")
        self.tabla.column("descripcion",width=300, anchor="w")
        self.tabla.heading("precio_unitario", text= "Precio unitario")
        self.tabla.column("precio_unitario",width=90, anchor="w")
        self.tabla.heading("stock", text= "Stock actual")
        self.tabla.column("stock",width=90, anchor="w")
        self.tabla.heading("id_marca", text= "ID Marca")
        self.tabla.column("id_marca",width=90, anchor="w")
        self.tabla.heading("id_categoria", text= "ID Categoría")
        self.tabla.column("id_categoria",width=90, anchor="w")

        self.tabla.pack()
        # Vincular el evento de selección de un registro de la tabla
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionarRegistro)

        # Cargar los datos de la base de datos y actualizarlos en la tabla
        self.actualizarVistaTabla()
        
        if callback:
            regresar= Button(base, text="Volver al menú", command=callback).pack(pady=10)

    
    # Método para guardar registros en la base de datos
    def guardarRegistros(self):
        try:
            # Obtener los valores de los campos de entrada
            self.obtenerTexto()

            # Llamar a la función para agregar un producto
            manejarProducto.IngresarProducto(self.nom, self.desc, self.precio, self.stock, self.marca, self.categoria)
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
            datos = manejarProducto.MostrarProducto()

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


        except Exception as error:
            # Si hay un error, se imprime en la consola
            print("Error al seleccionar:", error)

    # Método para modificar un registro existente en la base de datos
    def modificarRegistro(self):
        try:
            # Obtener los valores de los campos de entrada
            self.obtenerTexto()
            # Llamar a la función para modificar los datos del cliente
            manejarProducto.ModificarProducto(self.id,self.nom, self.desc, self.precio, self.stock, self.marca, self.categoria)
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
            producto_a_eliminar = self.textId.get()

            # Llamar a la función para eliminar el cliente
            manejarProducto.EliminarProducto(producto_a_eliminar)
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
        self.textNom.delete(0, END)
        self.textD.delete(0, END)
        self.textPrecio.delete(0, END)
        self.textSt.delete(0, END)
        self.textMarca.delete(0, END)
        self.textCat.delete(0, END)
    
    def insertarTexto(self,values):
        self.textId.insert(0, values[0])
        self.textNom.insert(0, values[1])               
        self.textD.insert(0, values[2])               
        self.textPrecio.insert(0, values[3])
        self.textSt.insert(0, values[4])
        self.textMarca.insert(0, values[5])
        self.textCat.insert(0, values[6])
    
    def obtenerTexto(self):
            self.id = self.textId.get()
            self.nom = self.textNom.get()
            self.desc = self.textD.get()
            self.precio = float(self.textPrecio.get())
            self.stock= int(self.textSt.get())
            self.marca= manejarProducto.obtenerId_marca(self.textMarca.get())
            self.categoria= manejarProducto.obtenerId_categoria(self.textCat.get())