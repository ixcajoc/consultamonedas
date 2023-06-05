from lista_circular_doble_enlazada import ListaCircularDobleEnlazada
import requests
import json
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from ClaseBotonCss import BotonCss
import random
from Arbol_Binario4 import ArbolBinario
#from TablaHash import HashTable
#from Hash4 import TablaHash
from Hash5 import TablaHash

lista = ListaCircularDobleEnlazada()


ventana = tk.Tk()
ventana.title("Consumo de API, solo para machos")
ventana.geometry("1200x700")
ventana.configure(background='#FFFFFF')
#ventana.overrideredirect(True)

def cerrar_ventana():
    ventana.destroy()

#defino los frames para acomodar los controles como lo desee
frame1 = Frame(ventana, bg="#0ba6ab", width=980,height=150)
frame1.place(x=220,y=0)
frame2 = Frame(ventana, bg="#14777a", width=220,height=220)
frame2.place(x=0,y=0)
frame3 = Frame(ventana, bg="#c7e5f7", width=220,height=480)
frame3.place(x=0,y=220)
frame4 = Frame(ventana,  width=450,height=200, bg ='white', relief = 'groove', highlightbackground="#0ba6ab", highlightthickness=3)
frame4.place(x=240,y=200)
frame5 = Frame(ventana, width=450,height=210,  bg ='white',relief = 'groove',highlightbackground="#0ba6ab", highlightthickness=3)#buena, con somra
#frame5 = Frame(ventana, width=500,height=200, borderwidth = 3, relief = 'groove')#groove simple pero buena
frame5.place(x=240,y=410)
frame6 = Frame(ventana, width=500,height=420 , background="white")
#frame5 = Frame(ventana, width=400,height=420,  bg ='white',relief = 'groove',highlightbackground="#0ba6ab", highlightthickness=3)#buena, con somra
frame6.place(x=700,y=200)

# Creamos un botón personalizado de cierre
cerrar_btn = tk.Button(frame1, text="X", bg="red", fg="white", font=("Arial", 12),command=cerrar_ventana)
cerrar_btn.place(x=950, y=5)

#variable de fuentes
fuente = ('Lilita One',20, 'bold')
color = '#0ba6ab'
#color = "#14777A"
#etiqueta del titulo
lbTitulo = ttk.Label(frame1,text="Tasas de Cambio", background="#0ba6ab",foreground="#C7EAEF", font=('Faster One',55, 'bold'))
lbTitulo.place(x=60,y=20)

# Crear un campo de entrada de fecha
date_label2 = ttk.Label(frame4,text="Inicio:",  font=("Lilita One", 25, 'bold'), foreground=color, background="white")
date_label2.place(x=80,y=50)
date_entry2 = DateEntry(frame4, date_pattern='yyyy-mm-dd', width=12, background=color,font=("Lilita One", 15), foreground='white', borderwidth=2)
date_entry2.place(x=220,y=55)

date_label = ttk.Label(frame4,text="Fin:", font=("Lilita One", 25, 'bold'), foreground=color, background="white")
date_label.place(x=120,y=100)
date_entry = DateEntry(frame4, date_pattern='yyyy-mm-dd', width=12, background=color,font=("Lilita One", 15), foreground='white', borderwidth=2)
date_entry.place(x=220,y=110)

#etiqueta para colocar las monedas que se desean evaluar
lbMonedaBase = ttk.Label(frame5,text="Moneda Base:", font=fuente, foreground=color, background="white")
lbMonedaBase.place(x=20,y=50)
txtMonedaBase = ttk.Entry(frame5,width=12, justify="center", font=("Lilita One", 15), foreground="#0ba6ab")
txtMonedaBase.place(x=240,y=55)

#etiqueta para las monedas a evaluar
lbMonedas = ttk.Label(frame5,text="Preferencias:",font=fuente, foreground=color, background="white")
lbMonedas.place(x=30,y=100)
txtMonedas = ttk.Entry(frame5, width=12, justify="center",font=("Lilita One", 15), foreground="#0ba6ab")
#txtMonedas.insert(tk.END, "Todas")
txtMonedas.place(x=240,y=105)

#colocar enlaces a paginas en el frame 3
lbMiPagina = BotonCss(frame3, "https://ixcajoc.github.io/monedas/", text="Monedas Diponibles")
lbMiPagina2 = BotonCss(frame3, "https://ixcajoc.github.io/monedas/", text="Contáctanos")
lbMiPagina.configure(width=19 , height=2)
lbMiPagina2.configure(width=19, height=2)
lbMiPagina.place(x=2,y=40)
lbMiPagina2.place(x=2, y=100)

# Cargamos la imagen
#img = tk.PhotoImage(file="foto1.png").subsample(12)
img = tk.PhotoImage(file="logoEmpresa.png")
logo = tk.PhotoImage(file="umg.png").subsample(2)
presi = tk.PhotoImage(file="presi.png")

# Creamos la etiqueta y le asignamos la imagen
label = tk.Label(frame2, image=img, borderwidth=0, highlightthickness=0)
label.pack(fill="both", expand=True)

lbLogo = tk.Label(frame1, image=logo,  borderwidth=0, highlightthickness=0)
lbLogo.place(x=820,y=1)

lbPresi = tk.Label(frame3, image=presi, borderwidth=0, highlightthickness=0)
lbPresi.place(x=1,y=230)

# Función para imprimir los valores ingresados
def print_values():
    fechaInicial = date_entry2.get()
    fechaFinal = date_entry.get()
    monedaBase = txtMonedaBase.get()
    monedasConsulta = txtMonedas.get()
    
    # print(f"Fecha de Inicio: {fechaInicial}")
    # print(f"Fecha de finalizacion: {fechaFinal}")
    # print(f"Moneda Base: {monedaBase}")
    # print(f"monedas Consulta: {monedasConsulta}")
    
    if monedasConsulta== "":
        url = f"https://api.apilayer.com/exchangerates_data/timeseries?start_date={fechaInicial}&end_date={fechaFinal}&base={monedaBase}"
    else:
        url = f"https://api.apilayer.com/exchangerates_data/timeseries?start_date={fechaInicial}&end_date={fechaFinal}&base={monedaBase}&symbols={monedasConsulta}"
    
    #ESTO TAMBIEN FUNCIONA
    #url = f"https://api.apilayer.com/exchangerates_data/timeseries?start_date={fechaInicial}&end_date={fechaFinal}&base={monedaBase}"
    #url = f"https://api.apilayer.com/exchangerates_data/timeseries?start_date={fechaInicial}&end_date={fechaFinal}&base={monedaBase}&symbols={monedasConsulta}"
    
    payload = {}
    headers= {
      #esta es la mia"apikey": "SIpoIlhvUlILl1VREi1QAHXApcp8R8Ez"
      "apikey": "gue644ewWDTwuWptWBDnt9LCRbefgAvZ"
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    status_code = response.status_code
    result = response.text
    base_datos = json.loads(result)
    
    
    #aca hacemos la cuenta de el total de monedas que hemos solcitado a la appi
    #para usarlo en el range de numeros aleatorios
    rates = base_datos['rates']
    listaMonedas = []
    for i in rates:
        for i,j in rates[i].items():
            listaMonedas.append(i)#los guarda una vez si estan repetidos
    totalMonedas = len(listaMonedas)
    print(totalMonedas)
    
    #Aca hacemos una lista para el combobox de moneda base
    monedas_para_combo_box = []
    for i in rates:
        for i,j in rates[i].items():
            monedas_para_combo_box.append(i)
        break
    

    #generamos una lista con numeros aleatorios 
    lista_numeros_aleatorios = list(range(0, totalMonedas)) # Crear una lista de números del 0 al numero total de monedas consultadas
    random.shuffle(lista_numeros_aleatorios) # Barajar aleatoriamente la lista
    contador = 0

    monedas = base_datos['rates']
    #llenamos los nodos
    for x in monedas:
        for i,j in monedas[x].items():
            #numero_aleatorio = random.randint(0, totalMonedas)
            numero_aleatorio = lista_numeros_aleatorios[contador]
            lista.agregar_final(x,i,j,numero_aleatorio)
            contador+=1
            
    #lista.agregar_inicio("hoy","Denis Coin",100);

    #lista.recorrer_inicio_a_fin()
    #lista.recorrer_fin_a_inicio()
    return lista.primero


#tv (tree view) creamos la tabla
tabla = ttk.Treeview(frame6, columns=("col1","col2","col3") ,height=15)
tabla.column("#0",width=125)
tabla.column("col1",width=120, anchor=CENTER)
tabla.column("col2",width=120)
tabla.column("col3",width=80)

style = ttk.Style()
#style.configure('Treeview', font=('Arial', 14 ), foreground='#202F32' )
style.configure('Treeview', font=('calibri', 14 ), foreground='black' )
style.configure('Treeview.Heading', font=('Lilita One', 20), foreground='#0ba6ab')

tabla.heading("#0",text="Fecha", anchor=CENTER )
tabla.heading("col1",text="Moneda", anchor=CENTER)
tabla.heading("col2",text="Precio", anchor=CENTER)
tabla.heading("col3",text="ID", anchor=CENTER)
tabla.place(x=10, y=5)


#creo que deberia limpiar la estructura con un metodo para borrar todos los registros
def eliminar():
    lista.eliminar_todos()
    #borrarInformacion()
    tabla.delete(*tabla.get_children())
    #tabla.destroy()



arbol = ArbolBinario()
objetoHash = TablaHash()
def tablas():
    
    #borrarInformacion()
    lista.eliminar_todos()
    tabla.delete(*tabla.get_children())
    #aux = lista.primero
    aux = print_values()
    while aux:
        tabla.insert("", END, text=aux.fecha, values=(aux.moneda, aux.tasa,aux.id))
        arbol.agregar_nodo(aux.id,aux.fecha,aux.moneda,aux.tasa)
        # objetoHash.agregar(str(aux.id),aux)
        objetoHash.agregar(aux.id,aux)
        aux = aux.siguiente
        if aux == lista.primero:
            break
    
        
    
    
    
def generar_arbol_binario():
    arbol.dibujar_arbol()


def crear_tabla_hash():
    objetoHash.mostrar()



# Botón para enviar los valores ingresados
submit_button = ttk.Button(frame6, text="Enviar", width=30, command=tablas)
submit_button.place(x= 10, y=360)
submit_button.config(padding=(0,9))


# Botón para enviar los valores ingresados
botonArbol = ttk.Button(frame6, text="Arbol Binario", width=30, command=generar_arbol_binario)
botonArbol.place(x= 270, y=360)
botonArbol.config(padding=(0,9))

# Botón para tabla Hash
TablaHash = ttk.Button(frame6, text="Tabla Hash", width=30, command=crear_tabla_hash)
TablaHash.place(x= 100, y=400)
TablaHash.config(padding=(0,9))
# Ejecutar la ventana principal
ventana.mainloop()

