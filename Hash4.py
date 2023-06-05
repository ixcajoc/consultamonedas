import tkinter as tk
from tkinter import ttk

class TablaHash:
    def __init__(self):
        self.tabla = {}

    def agregar(self, clave, valor):
        # calcular el hash de la clave y guardar el valor en la tabla
        # self.clave = str(clave)
        self.tabla[hash(clave)] = valor

    def obtener(self, clave):
        # obtener el valor asociado con la clave de la tabla hash
        return self.tabla.get(hash(clave))

    def eliminar(self, clave):
        # eliminar la clave y su valor asociado de la tabla hash
        del self.tabla[hash(clave)]
    
    def mostrar(self):
        # crear la ventana emergente
        ventana = tk.Toplevel()
        ventana.title("Tabla Hash")

        # crear el cuadro de texto y el botón de búsqueda
        cuadro_texto = tk.Entry(ventana)
        cuadro_texto.pack()
        boton_buscar = tk.Button(ventana, text="Buscar", command=lambda: self.buscar(int(cuadro_texto.get()), ventana))
        boton_buscar.pack()

        # crear la tabla
        tabla = ttk.Treeview(ventana, columns=("clave", "fecha","moneda","valor","nodo"))
        tabla.heading("#0", text="Índice")
        tabla.heading("clave", text="Clave")
        tabla.heading("fecha", text="Fecha")
        tabla.heading("moneda", text="Moneda")
        tabla.heading("valor", text="Valor")
        tabla.heading("nodo", text="DirecNodo")


        # agregar las entradas de la tabla hash a la tabla
        for indice, (clave, valor) in enumerate(self.tabla.items()):
            tabla.insert("", "end", text=str(indice), values=(str(clave), valor.fecha,valor.moneda,valor.tasa,valor))
            

        # empaquetar la tabla y mostrar la ventana
        tabla.pack()
        ventana.mainloop()
    
    def buscar(self, clave, ventana):
        # buscar el valor asociado con la clave de la tabla hash
        valor = self.obtener(clave)

        # mostrar una ventana emergente con el valor si se encuentra
        if valor is not None:
            ventana_resultado = tk.Toplevel()
            ventana_resultado.title("Resultado de búsqueda")
            etiqueta_resultado = tk.Label(ventana_resultado, text=f"La clave {clave} tiene los valores \n Id:{valor.id}\n Fecha:{valor.fecha}\n Moneda:{valor.moneda}\n Valor:{valor.tasa}")
            etiqueta_resultado.pack()
        else:
            tk.messagebox.showerror("Error de búsqueda", f"No se encontró la clave '{clave}'")