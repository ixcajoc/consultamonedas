import tkinter as tk
from tkinter import ttk


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def hash_function(self, key):
        return key % self.size
    
    def insert(self, key, value):
        hash_key = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[hash_key]):
            if k == key:
                self.table[hash_key][i] = (key, value)
                break
        else:
            self.table[hash_key].append((key, value))
    
    def clave(self,key):
        return key

    def search(self, key):
        hash_key = self.hash_function(key)
        for k, v in self.table[hash_key]:
            if k == key:
                return v
        raise KeyError(key)

    def delete(self, key):
        hash_key = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[hash_key]):
            if k == key:
                del self.table[hash_key][i]
                return
        raise KeyError(key)
    
   
    def mostrar_tabla(self):
            # Crear una ventana emergente
            ventana = tk.Tk()
            ventana.title("Tabla hash")

            # Crear una tabla en la ventana emergente
            tabla = ttk.Treeview(ventana, columns=("ID", "Fecha", "Moneda", "Valor"), show="headings")
            tabla.heading("ID", text="ID")
            tabla.heading("Fecha", text="Fecha")
            tabla.heading("Moneda", text="Moneda")
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






    # crear_tabla(self,key):
    #     objetoTabla = HashTable()

    #     # Crear una ventana emergente
    #     ventana = tk.Tk()
    #     ventana.title("Tabla hash")

    #     # Crear una tabla en la ventana emergente
    #     tabla = ttk.Treeview(ventana, columns=("ID", "Fecha", "Nombre", "Valor"), show="headings")
    #     tabla.heading("ID", text="ID")
    #     tabla.heading("Fecha", text="Fecha")
    #     tabla.heading("Nombre", text="Nombre")
    #     tabla.heading("Valor", text="Valor")

    #     # Agregar datos a la tabla
    #     #for id, nodo in tabla_hash.items():
    #     Miclave = objetoTabla.clave()
    #     hash_key = objetoTabla.hash_function(Miclave)
    #     for id, nodo in objetoTabla[hash_key]:
    #         if id == Miclave:
    #             fecha = nodo.fecha
    #             moneda = nodo.moneda
    #             tasa = nodo.tasa
    #             id_nodo = nodo.id
    #             tabla.insert("", "end", values=(id_nodo, fecha, moneda, tasa))

    #     # Mostrar la tabla en la ventana emergente
    #     tabla.pack()

    #     # Ejecutar la ventana emergente
    #     ventana.mainloop()



# # Creamos una tabla hash con 10 "buckets"
# hash_table = HashTable(10)

# # Insertamos algunos pares clave-valor
# hash_table.insert(25,"Juan")
# hash_table.insert(30,"Ana")
# hash_table.insert(20,"Carlos")

# # Buscamos la edad de Ana
# edad_ana = hash_table.search(30)
# print(f"La edad de Ana es {edad_ana}")

# # Eliminamos a Carlos de la tabla
# hash_table.delete("Carlos")

# # Intentamos buscar la edad de Carlos (debería lanzar una excepción)
# edad_carlos = hash_table.search("Carlos")
