import tkinter as tk
from tkinter import ttk

#en esta version tratamos de colorear la linea de color amarillo y que tambine aparezca la ventana emergente con los datos
class TablaHash:
    def __init__(self):
        self.tabla = {}

    def agregar(self, clave, valor):
        # calcular el hash de la clave y guardar el valor en la tabla
        # self.clave = str(clave)
        self.tabla[hash(clave)] = valor

    def borrarTodo(self):
        #no estoy seguro de que funcione
        self.tabla = {}  # crear una nueva tabla hash vacía

    def obtener(self, clave):
        # obtener el valor asociado con la clave de la tabla hash
        return self.tabla.get(hash(clave))

    def eliminar(self, clave):
        # eliminar la clave y su valor asociado de la tabla hash
        del self.tabla[hash(clave)]
    
    def mostrar(self):
        # crear la ventana emergente
        ventana = tk.Toplevel()
        #ventana = tk.Tk()
        ventana.title("Tabla Hash")
        ventana.geometry("1000x323")

        # crear el cuadro de texto y el botón de búsqueda
        cuadro_texto = tk.Entry(ventana)
        cuadro_texto.configure(justify="center",font=("Lilita One", 13),foreground="#0ba6ab", width=15)
        cuadro_texto.place(x=40,y=10)
        #boton que colorea la fila de la clave buscada
        #boton_buscar = tk.Button(ventana, text="Buscar", command=lambda: self.buscar(int(cuadro_texto.get()), ventana))
        boton_buscar = tk.Button(ventana, text="Buscar", command=lambda: self.buscar(int(cuadro_texto.get()), tabla,ventana))
        boton_buscar.configure(font=("Lilita One", 13),foreground="#0ba6ab",background="white")
        boton_buscar.place(x=90,y=40)

        # crear el cuadro de texto y el botón de eliminar
        # cuadro_eliminar = tk.Entry(ventana)
        # cuadro_eliminar.configure(justify="center",font=("Lilita One", 13),foreground="#0ba6ab", width=15)
        # cuadro_eliminar.place(x=300,y=10)
        #boton que colorea la fila de la clave buscada
        #boton_buscar = tk.Button(ventana, text="Buscar", command=lambda: self.buscar(int(cuadro_texto.get()), ventana))
        #boton_eliminar = tk.Button(ventana, text="Eliminar", command=lambda: self.eliminarClave(int(cuadro_eliminar.get())))
        
        # #boton que muestra ventanita emergente con valores de la clave
        # boton_buscar = tk.Button(ventana, text="Mostrar valores de busqueda", command=lambda: self.buscar_ventana_emergente(int(cuadro_texto.get()), ventana))
        # boton_buscar.pack()

        # crear la tabla
        #show="headings quita la columna de indice"
        #tabla = ttk.Treeview(ventana, columns=("clave", "fecha","moneda","valor","nodo"),show="headings")
        tabla = ttk.Treeview(ventana, columns=("clave", "fecha","moneda","valor"))
        tabla.heading("#0", text="Índice")
        tabla.heading("clave", text="Clave")
        tabla.heading("fecha", text="Fecha")
        tabla.heading("moneda", text="Moneda")
        tabla.heading("valor", text="Valor")
        #tabla.column("#0",width=125)
        
        # agregar las entradas de la tabla hash a la tabla
        for indice, (clave, valor) in enumerate(self.tabla.items()):
            tabla.insert("", "end", text=str(indice), values=(str(clave), valor.fecha,valor.moneda,valor.tasa))
        
        # empaquetar la tabla y mostrar la ventana
        tabla.place(y=90)
        ventana.mainloop()

        

    def buscar(self, clave, tabla, ventana):
        for item_id in tabla.get_children():
            item = tabla.item(item_id)
            values = item['values']
            if int(values[0]) == clave:
                tabla.item(item_id, tags=('selected',))
            else:
                tabla.item(item_id, tags=())
        tabla.tag_configure('selected', background='#0ba6ab')#pintar amarilla la fila de la clave buscada

        # buscar el valor asociado con la clave de la tabla hash
        valor = self.obtener(clave)

        # mostrar una ventana emergente con el valor si se encuentra
        if valor is not None:
            ventana_resultado = tk.Toplevel()
            ventana_resultado.title("Resultado de búsqueda")
            etiqueta_resultado = tk.Label(ventana_resultado, text=f"  La clave {clave} tiene los valores:  \n \n  Id : {valor.id}\n  Fecha : {valor.fecha}\n  Moneda : {valor.moneda}\n  Valor : {valor.tasa}")
            etiqueta_resultado.configure(justify="left",font=("Arial", 13,"bold italic"),foreground="#0ba6ab", background="white")
            etiqueta_resultado.pack()
        else:
            tk.messagebox.showerror("Error de búsqueda", f"No se encontró la clave '{clave}'")

    def eliminarClave(self, clave,tabla):
        clave = self.cuadro_eliminar.get()
        for item_id in self.tabla.get_children():
            item = self.tabla.item(item_id)
            if int(item['values'][0]) == int(clave):
                self.tabla.delete(item_id)
                break    
        self.cuadro_eliminar.delete(0, 'end')        
        
        

    """
    def buscar_ventana_emergente(self, clave, ventana):
        # buscar el valor asociado con la clave de la tabla hash
        valor = self.obtener(clave)

        # mostrar una ventana emergente con el valor si se encuentra
        if valor is not None:
            ventana_resultado = tk.Toplevel()
            ventana_resultado.title("Resultado de búsqueda")
            etiqueta_resultado = tk.Label(ventana_resultado, text=f"  La clave {clave} tiene los valores:  \n \n  Id : {valor.id}\n  Fecha : {valor.fecha}\n  Moneda : {valor.moneda}\n  Valor : {valor.tasa}")
            etiqueta_resultado.configure(justify="left",font=("Arial", 13,"bold italic"),foreground="#0ba6ab", background="white")
            etiqueta_resultado.pack()
        else:
            tk.messagebox.showerror("Error de búsqueda", f"No se encontró la clave '{clave}'")
"""
    