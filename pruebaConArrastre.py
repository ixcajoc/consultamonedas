from ListaConArrastre import DropdownSelectionBox
#esta si sirve


# Crear una lista de opciones para mostrar en la lista desplegable
options = ["Opción 1", "Opción 2", "Opción 3", "Opción 4", "Opción 5","Opción 1", "Opción 2", "Opción 3", "Opción 4", "Opción 5","Opción 1", "Opción 2", "Opción 3", "Opción 4", "Opción 5","Opción 1", "Opción 2", "Opción 3", "Opción 4", "Opción 5","Opción 1", "Opción 2", "Opción 3", "Opción 4", "Opción 5"]

# Crear una instancia de la clase DropdownSelectionBox
dropdown_box = DropdownSelectionBox(options)

# Ejecutar la ventana y permitir al usuario seleccionar una o varias opciones
dropdown_box.run()
