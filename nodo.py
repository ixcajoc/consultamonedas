class Nodo:

    def __init__(self,fecha,moneda,tasa,id):
        #self.dato = dato
        self.fecha = fecha
        self.moneda = moneda
        self.tasa = tasa
        self.id = id
        self.siguiente = None
        self.anterior = None
        


        #el id, lo coloco en el arbol. Cuando seleccione id
        #se mostrara objeto.fecha. objeto.moneda. objeto.tasa y listo a mimir
