import colorama
import subprocess
import matplotlib.pyplot as plt
import numpy

subprocess.run("clear")

class Function(object):
    def __init__(self,*args):

        self.sum = 0
        self.args = args
        for x in range(0,len(args)):
            self.sum += args[x]**x

    def __str__(self):
        lista = []

        for x in range(0,len(self.args)):
            if x == 0 :
                if self.args[x]>=0:
                    lista.append("+" + str(self.args[x])+"")
                    continue
                lista.append("-" + str(self.args[x])+ "")
            elif self.args[x]>0:
                if x == len(self.args)-1:
                    lista.append(str(self.args[x])+"*x**"+ str(x)+"")
                    continue
                lista.append("+" + str(self.args[x])+"*x**"+ str(x)+ "")
            elif self.args[x]<0:
                lista.append("-" + str(self.args[x])[1::]+"*x**"+ str(x)+ "")

        lista.reverse()
        string = "".join(lista)
        
        return string
    
    def zamiana(self,wartosc):
        funkcja = str(self)
        funkcja = funkcja.replace('x',str(wartosc)) 
        funkcja = funkcja.replace("**",str("**"))
        return funkcja
    
    def oblicz(self,wartosc):
        self._wynik = eval(self.zamiana(wartosc))
        print(f"Wynikiem funkcji ({self}) dla x = {wartosc} jest : {self._wynik}")
        return self._wynik

wartosc = 55
obiekt = Function(5,5,55)# 5x**0 + 5x**1 + 55x**2
wynik = obiekt.oblicz(wartosc)# wynik: 166 655



