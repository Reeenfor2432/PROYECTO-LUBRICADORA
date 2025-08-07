import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from claseUtilitaria import claseUtilitaria

from db import conn, cursor

class vistaGenerarCita:
    def generarCita(self,base,callbackMenu):
        groupBoxdatos= LabelFrame(base, text= "Datos de la Cita", padx=10, pady=10)
        groupBoxdatos.pack(pady=50)

        labelId= Label(groupBoxdatos, text= "Identificación de cita (Solo en ELIMINAR):", width=35, font=("arial",12))
        labelId.grid(row=0, column=0)
        self.textId = tk.Entry(groupBoxdatos)
        self.textId.grid(row=0,column=1)

        labelNom= Label(groupBoxdatos, text="Identificación de cliente:", width=35, font=("arial",12))
        labelNom.grid(row=1, column=0)
        self.textNom = tk.Entry(groupBoxdatos)
        self.textNom.grid(row=1,column=1)

        labelP= Label(groupBoxdatos, text= "Placa de vehiculo a registrar:", width=35, font=("arial",12))
        labelP.grid(row=2, column=0)
        self.textP = tk.Entry(groupBoxdatos)
        self.textP.grid(row=2,column=1)

        labelEmp= Label(groupBoxdatos, text= "Identificación de empleado a asignar:", width=35, font=("arial",12))
        labelEmp.grid(row=3, column=0)
        self.textEmp = tk.Entry(groupBoxdatos)
        self.textEmp.grid(row=3,column=1)

        labeling= Label(groupBoxdatos, text= "Hora de ingreso (YYYY-MM-DD HH:MM:SS):", width=35, font=("arial",12))
        labeling.grid(row=4, column=0)
        self.texting = tk.Entry(groupBoxdatos)
        self.texting.grid(row=4,column=1)

        labelsal= Label(groupBoxdatos, text= "Hora de salida (YYYY-MM-DD HH:MM:SS):", width=35, font=("arial",12))
        labelsal.grid(row=5, column=0)
        self.textsal = tk.Entry(groupBoxdatos)
        self.textsal.grid(row=5,column=1)

        labelEst= Label(groupBoxdatos, text= "Estado(Opcional): ", width=25, font=("arial",12))
        labelEst.grid(row=6, column=0)
        self.textEst = tk.Entry(groupBoxdatos)
        self.textEst.grid(row=6,column=1)

        #Tabla para mostrar las citas
        self.tabla= claseUtilitaria.tablaParaCita(base)

        # Vincular el evento de selección de un registro de la tabla
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionarRegistro)

        # Cargar los datos de la base de datos y actualizarlos en la tabla
        self.actualizarVistaTabla()

        
        Button(groupBoxdatos, text="Generar",  width=15, command=self.generarCitaBD).grid(row=7, column=0)
        Button(groupBoxdatos, text="Modificar", width=15, command=self.modificarCitaBD).grid(row=7, column=1)
        Button(groupBoxdatos, text="Eliminar",  width=15, command=self.eliminarCitaBD).grid(row=7, column=2, padx=(40,40))
                    
        if callbackMenu:
            regresar= Button(base, text="Volver al menú", command=callbackMenu).pack(pady=10)
        
    #Metodos para los botones generar, modificar, eliminar... (Copiar y pegar de otras vistas)
    # ---------- INSERT ----------
    def generarCitaBD(self):
        sql = """INSERT INTO cita
         (id_cliente, placa, id_empleado, hora_ingreso, total, descuento)
         VALUES (%s,%s,%s,%s,0,0)"""
        datos = (self.textNom.get(),   
         self.textP.get(),
         self.textEmp.get(),    
         self.texting.get())
        cursor.execute(sql, datos)
        conn.commit()
        messagebox.showinfo("OK", "Cita generada.")
        self.actualizarVistaTabla()

    # ---------- UPDATE ----------
    def modificarCitaBD(self):
        sql = """UPDATE cita
                 SET hora_salida=%s, estado=%s
                 WHERE id_cita=%s"""
        datos = (self.textsal.get() or None,
                 self.textEst.get() or None,
                 self.textId.get())
        cursor.execute(sql, datos)
        conn.commit()
        messagebox.showinfo("OK", "Cita modificada.")
        self.actualizarVistaTabla()

    # ---------- DELETE ----------
    def eliminarCitaBD(self):
        cursor.execute("DELETE FROM cita WHERE id_cita=%s",
                       (self.textId.get(),))
        conn.commit()
        messagebox.showinfo("OK", "Cita eliminada.")
        self.actualizarVistaTabla()

    # ---------- REFRESCO tabla ----------
    def actualizarVistaTabla(self):
        cursor.execute("""SELECT id_cita, id_cliente, placa, id_empleado,
                                    hora_ingreso, hora_salida, estado
                            FROM cita""")
        filas = cursor.fetchall()          # ← lista de dicts
        self.tabla.delete(*self.tabla.get_children())

        for row in filas:
            valores = (row["id_cita"],
                        row["id_cliente"],
                        row["placa"],
                        row["id_empleado"],
                        row["hora_ingreso"],
                        row["hora_salida"],
                        row["estado"])
            self.tabla.insert("", tk.END, values=valores)

            
    # ---------- SELECT en tabla ----------
    def seleccionarRegistro(self, event):
        valores = self.tabla.item(self.tabla.focus())["values"]
        if valores:
            (cid, cli, pla, emp, hin, hsal, est) = valores
            self.textId.delete(0, tk.END);  self.textId.insert(0, cid)
            self.textNom.delete(0, tk.END); self.textNom.insert(0, cli)
            self.textP.delete(0, tk.END);   self.textP.insert(0, pla)
            self.textEmp.delete(0, tk.END); self.textEmp.insert(0, emp)
            self.texting.delete(0, tk.END); self.texting.insert(0, hin)
            self.textsal.delete(0, tk.END); self.textsal.insert(0, hsal)
            self.textEst.delete(0, tk.END); self.textEst.insert(0, est)


