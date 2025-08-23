import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Guardado_de_datos.AdminRoles import manejarRol
from claseUtilitaria import claseUtilitaria

class vistaRol:

    def pantallaRol(self, base, callbackMenu):
        self.base = base

        box = LabelFrame(base, text="Datos del Rol", padx=10, pady=10)
        box.pack(pady=20)

        Label(box, text="ID (Solo en ELIMINAR):", width=25, font=("arial",12)).grid(row=0, column=0)
        self.txtId = Entry(box); self.txtId.grid(row=0, column=1)

        Label(box, text="Nombre del rol:", width=25, font=("arial",12)).grid(row=1, column=0)
        self.txtNom = Entry(box); self.txtNom.grid(row=1, column=1)

        Label(box, text="Descripción:", width=25, font=("arial",12)).grid(row=2, column=0)
        self.txtDes = Entry(box); self.txtDes.grid(row=2, column=1)

        # Botones
        Button(box, text="Agregar",  width=12, command=self.add).grid(row=3, column=0, pady=5)
        Button(box, text="Modificar",width=12, command=self.update).grid(row=3, column=1)
        Button(box, text="Eliminar", width=12, command=self.delete).grid(row=3, column=2)

        # Tabla
        self.tabla = claseUtilitaria.tablaParaRol(base)
        self.tabla.bind("<<TreeviewSelect>>", self.cargarRegistro)
        self.refrescar()

        if callbackMenu:
            Button(base, text="Volver al menú", command=callbackMenu).pack(pady=10)

    # Métodos CRUD usando AdminRol
    def add(self):
        ok, msg = manejarRol.IngresarRol(self.txtNom.get(), self.txtDes.get())
        messagebox.showinfo("Resultado", msg)
        if ok: self.refrescar()

    def update(self):
        ok, msg = manejarRol.ModificarRol(self.txtId.get(), self.txtNom.get(), self.txtDes.get())
        messagebox.showinfo("Resultado", msg)
        if ok: self.refrescar()

    def delete(self):
        ok, msg = manejarRol.EliminarRol(self.txtId.get())
        messagebox.showinfo("Resultado", msg)
        if ok: self.refrescar()

    def refrescar(self):
        rows = manejarRol.MostrarRoles()
        self.tabla.delete(*self.tabla.get_children())
        for r in rows:
            self.tabla.insert("", tk.END, values=(r["id_rol"], r["nombre_rol"], r["descripcion"]))

    def cargarRegistro(self, _):
        vals = self.tabla.item(self.tabla.focus())["values"]
        if vals:
            self.txtId.delete(0, END); self.txtId.insert(0, vals[0])
            self.txtNom.delete(0, END); self.txtNom.insert(0, vals[1])
            self.txtDes.delete(0, END); self.txtDes.insert(0, vals[2])