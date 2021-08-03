from OperacionNumero import Intermedio


class OperacionLista(Intermedio):

    def __init__(self, lista):
        self.__lista = lista
   

    def presentarLista(self):
        print(self.__lista)

    def buscarLista(self, valor):
        mensaje = f"ha encontrado el valor '{valor}'"
        print(f"Se {mensaje}" if valor in self.__lista else f"No se {mensaje}")

    def listaFactorial(self):
        self.presentarLista()
        print (f"tipo de lista{type(self.__lista)}")
        for i in self.__lista:
            print(Intermedio().factorial(i))

    def listaPrimo(self):
        self.presentarLista()
        for i in self.__lista:
            Intermedio().primo(i)

    def listaNotas(self, listaNotasDicccionario):
        self.mostrar_dictionary(listaNotasDicccionario)

    def insertarLista(self, valor, posicion):
        self.__lista.insert(posicion, valor)

    def eliminarLista(self, valor):
        self.buscarLista(valor)
        if valor in self.__lista:
            self.__lista.pop(self.__lista.index(valor))
            print(f"Se ha eliminado el valor '{valor}'")

    def retornaValorLista(self, posicion):  
        if posicion <= len (self.__lista):
            print(
                f"El numero {self.__lista[posicion-1]} se encuentra en la posicion {posicion-1}"
            )
            list(self.__lista).remove(self.__lista[posicion-1])
            return self.__lista[posicion-1]
        else:
            print(f"La poscicion debe ser menor a {len (self.__lista)}")

    def copiarTuplaLista(self, tupla):
        lista = []
        for i in range(len(tupla)):
            lista.append(tupla[i])
        print(f"Lista: {lista} ")

    def vueltoLista(self, listaClientesDiccionario: dict):
        self.mostrar_dictionary(listaClientesDiccionario)

    def mostrar_dictionary(self,lista):
        for llave, valor in lista.items():
            print(f"{llave}")
            print(f"{valor}")

