class Calculadora:		
    def __init__(self,numero1,numero2):
            self._num1=numero1
            self._num2=numero2
                    
    def suma(self):
            return self._num1+self._num2

    def resta(self):
            return self._num1-self._num2

    def multiplicacion(self):
            return self._num1*self._num2

    def division(self):
            return self._num1/self._num2    


class calEstandar(Calculadora):

     def __init__(self, numero1, numero2):
            super().__init__(numero1,numero2)  
               
     def multiplicacion(self):
            return super().multiplicacion()
    
     def exponente(self):         
         return pow(self._num1,self._num2)

     def valorAbsoluto(self,numero):
         return abs(numero) 
       
class calCientifica(Calculadora):
    PI=3.1614
       
    def __init__(self, numero1, numero2):
            super().__init__(numero1,numero2)
        

    def  circunferencia(self):
         return 2*self.PI*self._num1

    def areaCirculo(self):
        return self.PI*self._num1**2

    def areaCuadrado(self):
        return self._num1*self._num1
    

