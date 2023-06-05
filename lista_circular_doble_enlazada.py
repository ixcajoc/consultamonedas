from nodo import Nodo

class ListaCircularDobleEnlazada:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        if self.primero == None:
            return True
        else:
            return False

    def agregar_inicio(self, fecha,moneda,tasa,id):
        if self.vacia():
            self.primero = self.ultimo = Nodo(fecha,moneda,tasa,id)
        else:
            aux = Nodo(fecha,moneda,tasa,id)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
        self.__unir_nodos()

    def agregar_final(self, fecha,moneda,tasa,id):
        if self.vacia():
            self.primero = self.ultimo = Nodo(fecha,moneda,tasa,id)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(fecha,moneda,tasa,id)
            self.ultimo.anterior = aux
        self.__unir_nodos()

    def __unir_nodos(self):
        self.primero.anterior = self.ultimo
        self.ultimo.siguiente = self.primero

    def recorrer_inicio_a_fin(self):
        aux = self.primero
        while aux:
            print(f"Fecha: {aux.fecha}")
            print(f"Moneda: {aux.moneda}")
            print(f"Tasa: {aux.tasa}")
            print(f"Tasa: {aux.id}")
            print("___   ___   ___   ___   ___")

            
            aux = aux.siguiente
            if aux == self.primero:
                break

    def recorrer_fin_a_inicio(self):
        aux = self.ultimo
        while aux:
            print(f"Fecha: {aux.fecha}")
            print(f"Moneda: {aux.moneda}")
            print(f"Tasa: {aux.tasa}")
            print(f"Tasa: {aux.id}")
            print("___   ___   ___   ___   ___")
            aux = aux.anterior
            if aux == self.ultimo:
                break

    

    def eliminar_todos(self):
        if self.vacia():
            return

        # Desconectar los nodos
        aux = self.primero
        while aux.siguiente != self.primero:
            aux = aux.siguiente
            aux.anterior.siguiente = None
            aux.anterior = None

        # Establecer primero y ultimo a None
        self.primero = None
        self.ultimo = None