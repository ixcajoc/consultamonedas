import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from PIL import Image

class Nodo:
    def __init__(self, valor,fecha,moneda,tasa):
        self.valor = valor
        self.fecha = fecha
        self.moneda = moneda
        self.tasa = tasa
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None
           
    def agregar_nodo(self, valor,fecha,moneda,tasa):
        nuevo_nodo = Nodo(valor,fecha,moneda,tasa)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self._agregar_nodo_recursivo(valor,fecha,moneda,tasa, self.raiz)
    
    #este metodo se usa en AGREGAR NODO
    def _agregar_nodo_recursivo(self, valor,fecha,moneda,tasa, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor,fecha,moneda,tasa)
            else:
                self._agregar_nodo_recursivo(valor,fecha,moneda,tasa, nodo_actual.izquierda)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor,fecha,moneda,tasa)
            else:
                self._agregar_nodo_recursivo(valor,fecha,moneda,tasa, nodo_actual.derecha)

    
    
    
    def dibujar_arbol(self):
        # Establecer el color de fondo del gráfico
        plt.gca().set_facecolor('#CAFAF7')

        if self.raiz is not None:
            self._dibujar_arbol_recursivo(self.raiz, 0, 0, 100)
        plt.show()
    
    def _dibujar_arbol_recursivo(self, nodo_actual, x, y, separacion):
        if nodo_actual is not None:
            izq_x = x - separacion
            der_x = x + separacion
            circulo = plt.text(x, y, str(nodo_actual.valor), color='white', fontsize=10, ha='center', va='center', bbox=dict(facecolor='#0CB219', edgecolor='black', boxstyle='circle'))

            def mostrar_hola(event, nodo_seleccionado):
                if event.artist == nodo_seleccionado:
                    tk.messagebox.showinfo(f"Nodo ID: {nodo_actual.valor}", f" Fecha: {nodo_actual.fecha}\n Moneda: {nodo_actual.moneda}\n Tasa: {nodo_actual.tasa}")
            
            circulo.set_picker(True)
            circulo.figure.canvas.mpl_connect('pick_event', lambda event: mostrar_hola(event, circulo))

            
            if nodo_actual.izquierda is not None:
                plt.plot([x, izq_x], [y-10, y-90], color='#845903')
                #self._dibujar_arbol_recursivo(nodo_actual.izquierda, izq_x, y-90, separacion//2)
                self._dibujar_arbol_recursivo(nodo_actual.izquierda, izq_x, y-90, separacion//2)
            if nodo_actual.derecha is not None:
                plt.plot([x, der_x], [y-10, y-90], color='#845903')
                #self._dibujar_arbol_recursivo(nodo_actual.derecha, der_x, y-90, separacion//2)
                self._dibujar_arbol_recursivo(nodo_actual.derecha, der_x, y-90, separacion//2)
