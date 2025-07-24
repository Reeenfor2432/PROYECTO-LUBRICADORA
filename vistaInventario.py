import tkinter as tk
from tkinter import *
from tkinter import ttk

class vistaInventario:
    def administrarInventario(self,base, callback=None):
        groupBox= LabelFrame(base, text="Datos del Producto", padx=10, pady=10 )
        groupBox.pack(pady=10)

        labelId= Label(groupBox, text= "Identificación del producto:", width=25, font=("arial",12))
        labelId.grid(row=0, column=0)
        textId= Entry(groupBox)
        textId.grid(row=0,column=1)

        labelNom= Label(groupBox, text= "Nombre del producto:", width=25, font=("arial",12))
        labelNom.grid(row=1, column=0)
        textNom= Entry(groupBox)
        textNom.grid(row=1,column=1)

        labelD= Label(groupBox, text= "Descripción", width=25, font=("arial",12))
        labelD.grid(row=2, column=0)
        textD= Entry(groupBox)
        textD.grid(row=2,column=1)

        labelPrecio= Label(groupBox, text= "Precio unitario", width=25, font=("arial",12))
        labelPrecio.grid(row=3, column=0)
        textPrecio= Entry(groupBox)
        textPrecio.grid(row=3,column=1)

        labelSt= Label(groupBox, text= "Stock actual:", width=25, font=("arial",12))
        labelSt.grid(row=4, column=0)
        textSt= Entry(groupBox)
        textSt.grid(row=4,column=1)

        labelMarca= Label(groupBox, text= "ID de marca", width=25, font=("arial",12))
        labelMarca.grid(row=5, column=0)
        textMarca= Entry(groupBox)
        textMarca.grid(row=5,column=1)

        labelCat= Label(groupBox, text= "ID de categoría", width=25, font=("arial",12))
        labelCat.grid(row=6, column=0)
        textCat= Entry(groupBox)
        textCat.grid(row=6,column=1)

        Button(groupBox, text= "Añadir", width=15).grid(row=7, column=0)
        Button(groupBox, text= "Modificar", width=15).grid(row=7, column=1)
        Button(groupBox, text= "Eliminar", width=15).grid(row=7, column=2, padx=(40,40))
        
        #Espacio para la tabla
        groupBox= LabelFrame(base,text="Lista de Productos", padx=5,pady=5,)
        groupBox.pack(pady=10)
        #Crecion de TreeView (widget que permite mostrar tablas)
        tabla= ttk.Treeview(groupBox,columns=("id_product","nombre_producto","descripcion", "precio_unitario", "stock", "id_Marca", "id_Categoria"), show="headings", height=5,)
        tabla.heading("id_product", text="Identificacion")
        tabla.column("id_product",width=100, anchor="w")
        tabla.heading("nombre_producto", text= "Nombre del producto")
        tabla.column("nombre_producto",width=130, anchor="w")
        tabla.heading("descripcion", text= "Descripcion")
        tabla.column("descripcion",width=300, anchor="w")
        tabla.heading("precio_unitario", text= "Precio unitario")
        tabla.column("precio_unitario",width=90, anchor="w")
        tabla.heading("stock", text= "Stock actual")
        tabla.column("stock",width=90, anchor="w")
        tabla.heading("id_Marca", text= "ID Marca")
        tabla.column("id_Marca",width=90, anchor="w")
        tabla.heading("id_Categoria", text= "ID Categoría")
        tabla.column("id_Categoria",width=90, anchor="w")

        tabla.pack()
        
        if callback:
            regresar= Button(base, text="Volver al menú", command=callback).pack(pady=10)
