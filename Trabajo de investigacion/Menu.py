from OperacionLista import OperacionLista
from Calculadora import Calculadora, calCientifica, calEstandar
from OperacionCadena import OperacionCadena  
from OperacionNumero import Basico,Intermedio
class Menu:
    def __init__(self, titulo="", opciones=[]):
        self._titulo = titulo
        self._opciones = opciones

    def interact(self):
        self.mostrar()
        opcion = int(self.get_opcion())
        if opcion == 1:
            MenuCalculadora(
                "Menu Calculadora",
                [
                    "1) Suma",
                    "2) Resta",
                    "3) Multiplicacion",
                    "4) Divicion",
                    "5) Exponenciacion",
                    "6) Valor Absoluto",
                    "7) Circunferencia",
                    "8) Area del Circulo",
                    "9) Area del Cuadrado",
                    "10) salir",
                ]
            ).interact()
        if opcion == 2:
            MenuOperacionNumero(
                "Menu Operación Numeros",
                [
                    "1)	Presentar los números de 1 a n",
                    "2)	Sumar los números de 1 a n",
                    "3)	Múltiplo de cualquier numero",
                    "4)	Presentar los divisores de un numero",
                    "5)	Numero Primo",
                    "6)	Factorial de cualquier numero",
                    "7)	Fibonacci de una serie de n números",
                    "8)	Perfecto",
                    "9)	Primos gemelos",
                    "10)	Números amigos",
                    "11)	Salir",
                ]
            ).interact()
        if opcion == 4:
            MenuOperacionCadena(
                "Menu Operaciones de Cadenas",
                [
                    "1)	Recorrer y presentar los datos de una cadena",
                    "2)	Buscar un carácter en una cadena",
                    "3)	Retornar una lista con la posiciones dado un carácter de la cadena",
                    "4)	Retornar una lista con todas las palabras de una cadena",
                    "5)	Retornar una cadena a partir de una lista",
                    "6)	Insertar un dato en una cadena dada lo Posición",
                    "7)	Eliminar todas las ocurrencias en una cadena",
                    "8)	Retornar cualquier valor de una cadena eliminándolo ",
                    "9)	Concatenar cadenas",
                    "10)	Salir",
                ]
            ).interact()
        if opcion == 3:
            MenuTratamientoLista(
                "Menu Tratamiento Listas",
                [
                    "1)	Recorrer y presentar los datos de una lista",
                    "2)	Buscar un valor en una lista",
                    "3)	Retornar una lista con los factoriales",
                    "4)	Retornar una lista de números primos",
                    "5)	Recorrer una lista de diccionario con notas de alumnos",
                    "6)	Insertar un dato en una Lista dada lo Posición",
                    "7)	Eliminar todas las ocurrencias en una Lista",
                    "8)	Retornar cualquier valor de una lista eliminándolo ",
                    "9)	Copiar cada elemento de una tupla en una lista",
                    "10)	Dar el vuelto a varios clientes",
                    "11) Insertar datos de la lista",
                    "12)	Salir",
                ]
            ).interact()

    def mostrar(self):
        print(self._titulo)
        for i in self._opciones:
            print(i)

    def isValid(self, numero):
        return numero > 0 and numero <= len(self._opciones)

    def get_opcion(self):
        numero = input("Opcion [1-{}]:".format(len(self._opciones)))
        while not self.isValid(int(numero)):
            print(
                "Error!!! Debes ingresar un numero del 1 al {}".format(
                    len(self._opciones)
                )
            )
            numero = input("Opcion [1-{}]:".format(len(self._opciones)))

        return numero


class MenuCalculadora(Menu):
    def __init__(self, titulo, opciones):
        super().__init__(titulo, opciones)
        self.__calculadora = " "
        self.__calculadoraCentifica = " "
        self.__calculadoraEstandar = " "

    def interact(self):
        opcion = 0

        while int(opcion) != 10:
            self.mostrar()
            opcion = int(self.get_opcion())
            if opcion < 6 or opcion == 9:
                n1, n2 = int(input("n1 >> ")), int(input("n2 >> "))
                self.__calculadora = Calculadora(n1, n2)
                self.__calculadoraCentifica = calCientifica(n1, n2)
                if opcion == 1:
                    print(self.__calculadora.suma())
                if opcion == 2:
                    print(self.__calculadora.resta())
                if opcion == 3:
                    print(self.__calculadora.multiplicacion())
                if opcion == 4:
                    print(self.__calculadora.division())
                if opcion == 5:
                    self.__calculadoraEstandar = calEstandar(n1, n2)
                    print(self.__calculadoraEstandar.exponente())
                if opcion == 9:
                    print(self.__calculadoraCentifica.areaCuadrado())
            elif opcion < 10:
                n1 = int(input("numero >> "))
                self.__calculadoraEstandar = calEstandar(0, 0)
                self.__calculadoraCentifica = calCientifica(n1, 0)
                if opcion == 6:
                    print(self.__calculadoraEstandar.valorAbsoluto(n1))
                if opcion == 7:
                    print(self.__calculadoraCentifica.circunferencia())
                opcion = self.get_opcion()
                if opcion == 8:
                    print(self.__calculadoraCentifica.areaCirculo())
                
class MenuOperacionNumero(Menu):
    def init(self, titulo, opciones):
        super().init(titulo, opciones)

    def interact(self):
        opcion = 0
        while int(opcion) != len(self._opciones):
            self.mostrar()
            opcion = int(self.get_opcion())
            if opcion == 1:
                n1=(int(input("ingresa un numero ")))
                Basico().numerosN(n1)
                #Basico().numerosN(int(input("ingresa un numero ")))
            if opcion == 2:
                Basico().suma_numeros(int(input("ingresa un numero ")))
            if opcion == 3:
                Basico().multiplo(int(input("ingresa un numero ")))
            if opcion == 4:
                Basico().divisor(int(input("ingresa un numero ")))

            if opcion == 5:
                Basico().primo(int(input("ingresa un numero ")))

            if opcion == 6:
               print (Intermedio().factorial(int(input("ingresa un numero "))))

            if opcion == 7:
                Intermedio().fibonacci(int(input("ingresa un numero ")))

            if opcion == 8:
                Basico().perfecto(int(input("ingresa un numero ")))

            if opcion == 9:
                Intermedio().primosGemelos(int(input("ingresa n1 ")),int(input("ingresa n2 ")))
            
            if opcion ==10:
                Intermedio().amigos(int(input("ingresa n1 ")),int(input("ingresa n2")))
            

class MenuOperacionCadena(Menu):
    def __init__(self, titulo, opciones):
        super().__init__(titulo, opciones)

    def interact(self):
        opcion = 0
        operacionCadena=OperacionCadena(input("ingresar la frase: "))
        while int(opcion) != len(self._opciones):
            self.mostrar()
            opcion = int(self.get_opcion())
            if opcion == 1:
                operacionCadena.recorrerCadena()
            if opcion == 2:
                operacionCadena.buscarCaracter(input("inserte un caracter: "))
            if opcion == 3:
                operacionCadena.listaPosiciones()
            if opcion == 4:
                operacionCadena.listaPalabras()

            if opcion == 5:
                operacionCadena.cadenaLista()

            if opcion == 6:
                pos= int(input("inserte una posicion: "))
                valor=input("inserte un valor: ")
                operacionCadena.insertarDato(valor,pos)


            if opcion == 7:
                operacionCadena.eliminarOcurrencias(input("inserte un valor: "))

            if opcion == 8:
                operacionCadena.retornaValor(int(input("inserte una posicion: ")))

            if opcion == 9:
                operacionCadena.concatenarCadena(input("inserte una lista: "))
            

class MenuTratamientoLista(Menu):
    def __init__(self, titulo, opciones):
        super().__init__(titulo, opciones)

    def interact(self):
        opcion = 0
        operacionlista=OperacionLista([])
        while int(opcion) != len(self._opciones):

            self.mostrar()
            opcion = int(self.get_opcion())
            if opcion == 1:
                operacionlista.presentarLista()
            if opcion == 2:
                operacionlista.buscarLista(input("inserte un valor: "))
            if opcion == 3:
                operacionlista.listaFactorial()
            if opcion == 4:
                operacionlista.listaPrimo()

            if opcion == 5:
                diccionario = {}
                i = 0
                while i < 3:
                    diccionario['nombre']= input("ingresa el nombre del estudiante ")
                    diccionario['nota']= input("ingresa la nota del estudiante ")
                    i+=1
                OperacionCadena().listaNotas(diccionario)
                    
            if opcion == 6:
                operacionlista.insertarLista(int(input("valor ")),int(input("posicion ")))
            
            if opcion == 7:
                operacionlista.eliminarLista(input("inserte una lista: "))

            if opcion == 8:
                operacionlista.retornaValorLista(int(input("inserte una posicion: ")))
                
                
            if opcion == 9:

                operacionlista.copiarTuplaLista((1,2,3,4,5,6,7,8))

            if opcion == 10:
                diccionario = {}
                i = 0
                while i < 3:
                    diccionario['nombre']= input("ingresa del cliente")
                    diccionario['nota']= input("monto  ")
                    i+=1
                operacionlista.vueltoLista(diccionario)
            if opcion ==11:
                numeros=input("ingresar una lsita de numeros[1 2 3 4 ]:")
                numeros=numeros.replace(" ","")
                lista=[]
                for i in numeros:
                    lista.append(int(i))
                operacionlista=OperacionLista(lista)
            
#hola
Menu(
    "Menu Principal:",
    [
        "1) Calculadora",
        "2) Operacion Numeros",
        "3) Tratamiento de Listas",
        "4) Operaciones de  Cadenas",
        "5) Salir",
    ],
).interact()








