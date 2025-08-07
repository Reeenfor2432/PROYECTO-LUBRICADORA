# vistaServicios.py
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from claseUtilitaria import claseUtilitaria
from db import conn, cursor        # única conexión global

class vistaServicio:

    # --------------------------- UI principal ---------------------------
    def pantallaServicio(self, base, callbackMenu):
        group = LabelFrame(base, text="Datos del Servicio", padx=10, pady=10)
        group.pack(pady=20)

        # ------- entradas ----------
        Label(group, text="ID (Solo en ELIMINAR):").grid(row=0, column=0, sticky="e")
        self.txtId     = Entry(group, width=8);  self.txtId.grid(row=0, column=1)

        Label(group, text="Nombre del servicio:").grid(row=1, column=0, sticky="e")
        self.txtNombre = Entry(group, width=30); self.txtNombre.grid(row=1, column=1)

        Label(group, text="Precio:").grid(row=2, column=0, sticky="e")
        self.txtPrecio = Entry(group, width=10); self.txtPrecio.grid(row=2, column=1, sticky="w")

        # ------- botones CRUD -------
        btns = Frame(group); btns.grid(row=3, column=0, columnspan=2, pady=5)
        Button(btns, text="Agregar",  width=12, command=self.add).pack(side=LEFT, padx=4)
        Button(btns, text="Modificar",width=12, command=self.update).pack(side=LEFT, padx=4)
        Button(btns, text="Eliminar", width=12, command=self.delete).pack(side=LEFT, padx=4)

        # ------- tabla -------
        self.tabla = claseUtilitaria.tablaParaServicio(base)
        self.tabla.bind("<<TreeviewSelect>>", self.cargarFila)
        self.refrescar()

        # botón volver
        if callbackMenu:
            Button(base, text="Volver al menú", command=callbackMenu).pack(pady=10)

    # --------------------------- CRUD SQL ---------------------------
    def add(self):
        try:
            sql = "INSERT INTO servicio(nombre, precio) VALUES(%s,%s)"
            cursor.execute(sql, (self.txtNombre.get(), self.txtPrecio.get()))
            conn.commit()
            messagebox.showinfo("OK", "Servicio agregado.")
            self.refrescar()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update(self):
        try:
            sql = "UPDATE servicio SET nombre=%s, precio=%s WHERE id_servicio=%s"
            cursor.execute(sql, (self.txtNombre.get(), self.txtPrecio.get(), self.txtId.get()))
            conn.commit()
            messagebox.showinfo("OK", "Servicio modificado.")
            self.refrescar()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete(self):
        try:
            cursor.execute("DELETE FROM servicio WHERE id_servicio=%s", (self.txtId.get(),))
            conn.commit()
            messagebox.showinfo("OK", "Servicio eliminado.")
            self.refrescar()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # --------------------------- helpers ---------------------------
    def refrescar(self):
        cursor.execute("SELECT id_servicio, nombre, precio FROM servicio")
        rows = cursor.fetchall()
        self.tabla.delete(*self.tabla.get_children())
        for r in rows:
            self.tabla.insert("", tk.END, values=(r["id_servicio"], r["nombre"], r["precio"]))

    def cargarFila(self, _):
        fila = self.tabla.item(self.tabla.focus())["values"]
        if fila:
            sid, nom, pre = fila
            self.txtId.delete(0, END);     self.txtId.insert(0, sid)
            self.txtNombre.delete(0, END); self.txtNombre.insert(0, nom)
            self.txtPrecio.delete(0, END); self.txtPrecio.insert(0, pre)
