class Basico:
    def numerosN(self,n):
        contador = 1
        while contador <= n:
            print(contador)
            contador += 1

    def suma_numeros(self,n):
        suma = 0
        #1+2+3+4+5
        cont=n
        while cont>0:
            suma += (cont)
            cont -= 1
        print(f"Suma: {suma}")

    def multiplo(self,numero):
        n=numero
        print(f"los multiplos del numero {numero} son {[numero*i for i in range (1,n+1)]}")

    def primo(self, numero):
        mensaje = f"El número {numero}"
        print(
            f"{mensaje} es primo"
            if self.suma_divisores(numero) == 1
            else f"{mensaje} no es primo"
        )

    def divisor(self, numero):
        print(f"los multiplos del numero {numero} son {self.divisores(numero)}")
    def divisores(self, numero):
        result = []
        for i in range(1, numero+1):
            if numero % i == 0:
                result.append(i)
        return result
    def suma_divisores(self, numero):
        suma = 0
        result = self.divisores(numero)
        result.pop()
        for i in result:
            suma += i
        return suma

    def perfecto(self, numero):
        mensaje = f"El número {numero}"
        print(
            f"{mensaje} es perfecto"
            if self.suma_divisores(numero) == numero
            else f"{mensaje} no es perfecto"
        )


class Intermedio(Basico):
    def numerosN(self, n):
        self.numerosN(n)

    def factorial(self, n):
        return 1 if (n == 1 or n == 0) else n * self.factorial(n - 1)

    def fibonacci(self, n):
        n1, n2 = 0, 1
        sum = 0
        if n <= 0:
            print("Ingresa un numero mayor a cero")
        else:
            for i in range(0, n):
                print(sum, end=" ")
                n1 = n2
                n2 = sum
                sum = n1 + n2
        print()
    def primosGemelos(self,num1, num2):
        condition = (num1 - num2) == 2
        mensaje = f"El numero {num1} y {num2}"
        print(
            f"{mensaje} son primos gemelos"
            if condition
            else f"{mensaje} no son primos gemelos"
        )

    def amigos(self, num1, num2):
        condition = (
            self.suma_divisores(num1) == num2 and self.suma_divisores(num2) == num1
        )
        mensaje = f"El numero {num1} y {num2}"
        print(f"{mensaje} son amigos" if condition else f"{mensaje} no son amigos")



