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
                lista.append("" + str(self.args[x])+ "")
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

    def __sub__(self,other):
        print ("INFORMATIONS:")
        print(colorama.Fore.WHITE + str(self) + f" --> {self.args}")
        print(str(other) + f" --> {other.args}")

        print(colorama.Fore.CYAN + f"\n({str(self)})-({str(other)}) ==>",end="")

        maximum = max(len(other.args),len(self.args))

        self.result = []

        for x in range(0,maximum):
            try: 
                self.result.append(self.args[x]-other.args[x])
            except:
                try: 
                    self.result.append(self.args[x])
                except:
                    self.result.append(other.args[x])

        return switch(self.result),self.result


def compareWithComputer(function, wartosc):
    funkcja = str(function)
    funkcja = funkcja.replace('x',str(wartosc)) 
    result = eval(funkcja)

    try:
        assert result == function.oblicz(wartosc)
        print(colorama.Fore.GREEN+ f"({function}) passsed the test with x == {wartosc} and result is {result}")
    except:
        print(colorama.Fore.RED + f"({function}) didnt pass the test with x =={wartosc} \n Result from ({function}) built in method : {function.oblicz(wartosc)}\n Correct result : {result}")
    print(colorama.Fore.WHITE, end="")


def compareWithYourResult(function, wartosc,result):

    try:
        assert result == function.oblicz(wartosc)
        print(colorama.Fore.GREEN+ f"({function}) passsed the test with x == {wartosc} and result is {result}")
    except:
        print(colorama.Fore.RED + f"Your result for ({function}) with x == {wartosc} isn't correct.\n Your result : {result}\n Correct result : {function.oblicz(wartosc)}")
    print(colorama.Fore.WHITE, end="")

def switch(args):
    lista = []

    for x in range(0,len(args)):
            if x == 0 :
                if args[x]>=0:
                    lista.append("+" + str(args[x])+"")
                    continue
                lista.append("" + str(args[x])+ "")
            elif args[x]>0:
                if x == len(args)-1:
                    lista.append(str(args[x])+"*x**"+ str(x)+"")
                    continue
                lista.append("+" + str(args[x])+"*x**"+ str(x)+ "")
            elif args[x]<0:
                lista.append("-" + str(args[x])[1::]+"*x**"+ str(x)+ "")

    lista.reverse()
    string = "".join(lista)
        
    return string


# wartosc = 55
# obiekt = Function(5,0,55)# 5x**0 + 0x**1 + 55x**2
# wynik = obiekt.oblicz(wartosc)# wynik: 166 380

# compareWithComputer(obiekt, 55)
# compareWithYourResult(obiekt, 55, 166_380)

# for x in range(-5999,5999):
#     compareWithComputer(obiekt,x)


obiekt1 = Function(2,0,-3,5) # 5x**3 - 3x**2 + 2
obiekt2 = Function(2,2,2)   # 2x**2 + 2x + 2
wynik, wynikArgs = obiekt1-obiekt2

print(" " + str(wynik) + colorama.Fore.GREEN + f"\ntuple wynikArgs: {tuple(wynikArgs)} <-- parameters that you have to put in the Function(wynikArgs:tuple) to initialize this function." + colorama.Fore.RED + "\nWARNING: YOU HAVE TO PUT IT MANUALLY")
print(colorama.Fore.WHITE,end="")

obiekt3 = Function(0,-2,-5,5)
print(f"test: {obiekt3}, input parameters: {tuple(wynikArgs)}")



