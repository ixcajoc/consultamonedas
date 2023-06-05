import tkinter as tk

# Función para mostrar la ventana emergente
def mostrar_ventana_emergente():
    ventana_emergente = tk.Toplevel(root)
    ventana_emergente.title("Ventana emergente")
    ventana_emergente.geometry("200x200")
    
    # Agregar elementos a la ventana emergente
    etiqueta = tk.Label(ventana_emergente, text="Esta es una ventana emergente")
    etiqueta.pack(padx=10, pady=10)

# Crear la ventana principal
root = tk.Tk()
root.title("Ventana principal")
root.geometry("400x400")

# Crear un botón que muestre la ventana emergente al hacer clic
boton = tk.Button(root, text="Mostrar ventana emergente", command=mostrar_ventana_emergente)
boton.pack(padx=50, pady=50)

# Iniciar el loop principal de la ventana
root.mainloop()
