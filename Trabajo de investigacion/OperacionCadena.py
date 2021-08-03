from OperacionNumero import Intermedio


class OperacionCadena(Intermedio):
    def __init__(self, cadena):
        self.cadena = cadena

    def recorrerCadena(self):
        for i in self.cadena:
            print(i)

    def buscarCaracter(self, caracter):
        mensaje = f"ha encontrado el caracter '{caracter}'"
        found = False
        for i in self.cadena:
            if i == caracter:
                found = True

        print(f"Se {mensaje}" if found else f"No se {mensaje}")

    def listaPosiciones(self, caracter):
        mensaje = f"ha encontrado el caracter '{caracter}'"
        positions = []
        index = 0
        for i in self.cadena:
            if i == caracter:
                positions.append(index)
            index += 1
        print(f"{mensaje} en las posiciones {positions}")

    def listaPalabras(self):
        print("Listado de palabras")
        for i in self.cadena.split():
            print(i)

    def cadenaLista(self):
        print(f"Cadena a lista {self.cadena.split()}")

    def insertarDato(self, insert, posicion):
        print(f"Se ha insertado {insert} en la posicion {posicion}")
        print(self.cadena[:posicion] + insert + self.cadena[posicion:])

    def eliminarOcurrencias(self, caracter):
        if caracter in self.cadena:
            print(self.cadena)
            print(f"Se ha eliminado la ocurrencia '{caracter}'")
            print(self.cadena.replace(caracter, "").strip())

    def retornaValor(self, posicion):
        print(
            f"En la poisicion {posicion} se encuentra el caracter {self.cadena[posicion]}"
        )

    def concatenarCadena(self, cadena):
        print(self.cadena)
        print(f"Se ha concatenado la cadena '{cadena}'")
        print(self.cadena + " " + cadena)



