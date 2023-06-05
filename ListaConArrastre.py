import tkinter as tk
from tkinter import ttk

#este si sirve

class DropdownSelectionBox:
    def __init__(self, options):
        self.options = options
        self.selected_options = []

        self.root = tk.Tk()

        self.option_menu = tk.Listbox(self.root, selectmode=tk.MULTIPLE, exportselection=False)
        self.option_menu.pack(fill='both', expand=True)

        for option in self.options:
            self.option_menu.insert(tk.END, option)

        self.option_menu.bind('<B1-Motion>', self.select_range)
        self.option_menu.bind('<Shift-Button-1>', self.select_range)

        button = tk.Button(self.root, text="Aceptar", command=self.print_selected)
        button.pack()

    def select_range(self, event):
        index = self.option_menu.nearest(event.y)
        if self.option_menu.selection_includes(index):
            return
        start, *_, end = sorted((self.option_menu.curselection() + (index,)))

        self.option_menu.selection_clear(0, start)
        self.option_menu.selection_set(start, end)
        self.option_menu.activate(index)

    

    def print_selected(self):
        self.selected_options.clear()
        selection = self.option_menu.curselection()
        for index in selection:
            self.selected_options.append(self.option_menu.get(index))
        print("Opciones seleccionadas:", ", ".join(self.selected_options))

    def run(self):
        self.root.mainloop()
