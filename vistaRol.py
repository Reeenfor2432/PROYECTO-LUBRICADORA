import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from claseUtilitaria import claseUtilitaria
from db import conn, cursor         

class vistaRol:

    def pantallaRol(self, base, callbackMenu):
        box = LabelFrame(base, text="Datos del Rol", padx=10, pady=10)
        box.pack(pady=40)

        # --------- Entradas ----------
        Label(box, text="ID (Solo en ELIMINAR):").grid(row=0, column=0, sticky="e")
        self.txtId  = tk.Entry(box); self.txtId.grid(row=0, column=1)

        Label(box, text="Nombre del rol:").grid(row=1, column=0, sticky="e")
        self.txtNom = tk.Entry(box); self.txtNom.grid(row=1, column=1)

        Label(box, text="Descripción:").grid(row=2, column=0, sticky="e")
        self.txtDes = tk.Entry(box); self.txtDes.grid(row=2, column=1)

        # --------- Botones ----------
        Button(box, text="Agregar",  width=12, command=self.agregarRol).grid(row=3, column=0, pady=5)
        Button(box, text="Modificar",width=12, command=self.modificarRol).grid(row=3, column=1)
        Button(box, text="Eliminar", width=12, command=self.eliminarRol).grid(row=3, column=2)

        if callbackMenu:
            Button(base, text="Volver al menú", command=callbackMenu).pack(pady=10)

        # --------- Tabla ----------
        self.tabla = claseUtilitaria.tablaParaRol(base)   # 3 columnas
        self.tabla.bind("<<TreeviewSelect>>", self.cargarRegistro)
        self.refrescarTabla()

    # ---------- INSERT ----------
    def agregarRol(self):
        sql = "INSERT INTO rol (nombre_rol, descripcion) VALUES (%s,%s)"
        datos = (self.txtNom.get(), self.txtDes.get())
        cursor.execute(sql, datos); conn.commit()
        messagebox.showinfo("OK", "Rol agregado.")
        self.refrescarTabla()

    # ---------- UPDATE ----------
    def modificarRol(self):
        sql = "UPDATE rol SET nombre_rol=%s, descripcion=%s WHERE id_rol=%s"
        datos = (self.txtNom.get(), self.txtDes.get(), self.txtId.get())
        cursor.execute(sql, datos); conn.commit()
        messagebox.showinfo("OK", "Rol modificado.")
        self.refrescarTabla()

    # ---------- DELETE ----------
    def eliminarRol(self):
        cursor.execute("DELETE FROM rol WHERE id_rol=%s", (self.txtId.get(),))
        conn.commit()
        messagebox.showinfo("OK", "Rol eliminado.")
        self.refrescarTabla()

    # ---------- REFRESH ----------
    def refrescarTabla(self):
        cursor.execute("SELECT id_rol, nombre_rol, descripcion FROM rol")
        filas = cursor.fetchall()
        self.tabla.delete(*self.tabla.get_children())
        for r in filas:
            self.tabla.insert("", tk.END, values=(r["id_rol"], r["nombre_rol"], r["descripcion"]))

    # ---------- CARGAR ---------
    def cargarRegistro(self, _):
        vals = self.tabla.item(self.tabla.focus())["values"]
        if vals:
            self.txtId .delete(0, tk.END); self.txtId .insert(0, vals[0])
            self.txtNom.delete(0, tk.END); self.txtNom.insert(0, vals[1])
            self.txtDes.delete(0, tk.END); self.txtDes.insert(0, vals[2])
