import tkinter as tk
from tkinter import ttk

class TablaHash:
    def __init__(self):
        self.tabla = {}

    def agregar_nodo(self, clave, nodo):
        self.tabla[clave] = nodo

    def mostrar_tabla(self):
        # Crear una ventana emergente
        ventana = tk.Tk()
        ventana.title("Tabla hash")

        # Crear una tabla en la ventana emergente
        tabla = ttk.Treeview(ventana, columns=("ID", "Fecha", "Nombre", "Valor"), show="headings")
        tabla.heading("ID", text="ID")
        tabla.heading("Fecha", text="Fecha")
        tabla.heading("Nombre", text="Nombre")
        tabla.heading("Valor", text="Valor")

        # Agregar datos a la tabla
        for id, nodo in self.tabla.items():
            fecha = nodo["fecha"]
            nombre = nodo["nombre"]
            valor = nodo["valor"]
            tabla.insert("", "end", values=(id, fecha, nombre, valor))

        # Mostrar la tabla en la ventana emergente
        tabla.pack()

        # Ejecutar la ventana emergente
        ventana.mainloop()
