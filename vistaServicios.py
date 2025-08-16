import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Guardado_de_datos.AdminServicios import manejarServicio
import claseUtilitaria

class vistaServicio:

    def pantallaServicio(self, base, callbackMenu):
        self.base = base

        group = LabelFrame(base, text="Datos del Servicio", padx=10, pady=10)
        group.pack(pady=20)

        Label(group, text="ID (Solo en ELIMINAR):", width=25, font=("arial",12)).grid(row=0, column=0)
        self.txtId = Entry(group); self.txtId.grid(row=0, column=1)

        Label(group, text="Nombre:", width=25, font=("arial",12)).grid(row=1, column=0)
        self.txtNombre = Entry(group); self.txtNombre.grid(row=1, column=1)

        Label(group, text="Descripción:", width=25, font=("arial",12)).grid(row=2, column=0)
        self.txtDesc = Entry(group); self.txtDesc.grid(row=2, column=1)

        Label(group, text="Precio:", width=25, font=("arial",12)).grid(row=3, column=0)
        self.txtPrecio = Entry(group); self.txtPrecio.grid(row=3, column=1)

        # Botones CRUD
        Button(group, text="Agregar",  width=12, command=self.add).grid(row=4, column=0, pady=5)
        Button(group, text="Modificar",width=12, command=self.update).grid(row=4, column=1)
        Button(group, text="Eliminar", width=12, command=self.delete).grid(row=4, column=2)

        # Tabla
        self.tabla = claseUtilitaria.tablaParaServicio(base)
        self.tabla.bind("<<TreeviewSelect>>", self.cargarRegistro)
        self.refrescar()

        if callbackMenu:
            Button(base, text="Volver al menú", command=callbackMenu).pack(pady=10)

    # CRUD usando AdminServicio
    def add(self):
        ok, msg = manejarServicio.IngresarServicio(self.txtNombre.get(), self.txtDesc.get(), self.txtPrecio.get())
        messagebox.showinfo("Resultado", msg)
        if ok: self.refrescar()

    def update(self):
        ok, msg = manejarServicio.ModificarServicio(self.txtId.get(), self.txtNombre.get(), self.txtDesc.get(), self.txtPrecio.get())
        messagebox.showinfo("Resultado", msg)
        if ok: self.refrescar()

    def delete(self):
        ok, msg = manejarServicio.EliminarServicio(self.txtId.get())
        messagebox.showinfo("Resultado", msg)
        if ok: self.refrescar()

    def refrescar(self):
        rows = manejarServicio.MostrarServicios()
        self.tabla.delete(*self.tabla.get_children())
        for r in rows:
            self.tabla.insert("", tk.END, values=(r["id_servicio"], r["nombre"], r["descripcion"], r["precio"]))

    def cargarRegistro(self, _):
        vals = self.tabla.item(self.tabla.focus())["values"]
        if vals:
            self.txtId.delete(0, END); self.txtId.insert(0, vals[0])
            self.txtNombre.delete(0, END); self.txtNombre.insert(0, vals[1])
            self.txtDesc.delete(0, END); self.txtDesc.insert(0, vals[2])
            self.txtPrecio.delete(0, END); self.txtPrecio.insert(0, vals[3])

