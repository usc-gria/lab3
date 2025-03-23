from nodo import Nodo


class ListaEnlazada:

    def __init__(self, dato=None):
        if dato is not None:
            self.__cabeza = Nodo(dato)
            self.__tamano = 1
        else:
            self.__cabeza = None
            self.__tamano = 0

    def get_cabeza(self):
        return self.__cabeza

    def set_cabeza(self, nodo):
        self.__cabeza = nodo

    def get_tamano(self):
        return self.__tamano

    def set_tamano(self, nuevo):
        self.__tamano = nuevo

    def vacia(self):
        return self.__tamano == 0

    def anade_elemento_cabeza(self, dato):
        segundo_nodo = self.get_cabeza()
        self.set_cabeza(Nodo(dato, segundo_nodo))
        self.__tamano = self.__tamano + 1

    def anade_elemento_final(self, dato):
        if self.vacia():
            self.set_cabeza(Nodo(dato))
        else:
            nodo = self.get_cabeza()
            while nodo.get_sig() is not None:
                nodo = nodo.get_sig()
            nodo.set_sig(Nodo(dato))
        self.set_tamano(self.__tamano+1)

    def imprime(self):
        nodo = None
        if not self.vacia():
            nodo = self.__cabeza
        else:
            print("La lista está vacía")
        while nodo is not None:
            print(nodo.get_dato(), end=" ")
            nodo = nodo.get_sig()
