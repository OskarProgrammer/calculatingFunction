import colorama
import subprocess

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
        return funkcja
    
    def oblicz(self,wartosc):
        self._wynik = eval(self.zamiana(wartosc))
        return self._wynik

def test(function, wartosc):
    funkcja = str(function)
    funkcja = funkcja.replace('x',str(wartosc)) 
    result = eval(funkcja)

    try:
        assert result == function.oblicz(wartosc)
        print(colorama.Fore.GREEN+ f"({function}) passsed the test with x == {wartosc} and result is {result}")
    except:
        print(colorama.Fore.RED + f"({function}) didnt pass the test with x =={wartosc} \n Result from ({function}) built in method : {function.oblicz(wartosc)}\n Correct result : {result}")
    print(colorama.Fore.WHITE, end="")



wartosc = 55
obiekt = Function(5,5,55)# 5x**0 + 5x**1 + 55x**2
wynik = obiekt.oblicz(wartosc)# wynik: 166 655

test(obiekt,55)



