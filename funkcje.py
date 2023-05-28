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
                    lista.append("+ " + str(self.args[x])+" ")
                    continue
                lista.append("- " + str(self.args[x])+ " ")
            elif self.args[x]>0:
                if x == len(self.args)-1:
                    lista.append(str(self.args[x])+"x**"+ str(x)+" ")
                    continue
                lista.append("+ " + str(self.args[x])+"x**"+ str(x)+ " ")
            elif self.args[x]<0:
                lista.append("- " + str(self.args[x])[1::]+"x**"+ str(x)+ " ")

        lista.reverse()
        string = "".join(lista)
        
        return string

def test(function,function_name):
    #setting variables
    result = 0
    args = function.args
    print(function)
    #calculating correct result
    for x in range (0,len(args)):
        result += args[x]**x

    #checking if result is equals to function.sum
    try:
        assert function.sum == float(result)
        print(colorama.Fore.GREEN + f"{function_name} passed !")
    except: 
        print(colorama.Fore.RED + f"{function_name} didnt pass the test,  Result from {function_name}: {function.sum}; result from test : {result}")
    print(colorama.Fore.WHITE,end="")

test(Function(1,2,3),"funkcja")
test(Function(5,-2), "funkcja 2")

obiekt = Function(0 ,-25,-2,2,2,2,1)
test(obiekt,"funkcja 3")

print(obiekt)
