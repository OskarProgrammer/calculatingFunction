
class Function(object):
    def __init__(self,function:str) -> None:
        self.function = function
        self.args = self.filtr()

    def convert(self,value:float)->str:
        self.function = self.function.replace("x",str(value))
        return self.function

    def calculate(self,value:float)-> float:
        self._result = eval(self.convert(value))
        
        return self._result
    
    def filtr(self):
        self._listaBanned = ["x","+","-","**1","**2"
                             ,"**3","**4","**5","*"]
        self.args = self.function

        for x in self._listaBanned:
            self.args = self.args.replace(str(x),"")
        self.args = list(self.args)
        
        return self.args

    def __str__(self):
        return str(self.function)

    def __sub__(self, other):
        print(other.args)
        print(self.args)
        self.result = []
        # if len(self.args)>len(other.args):
        #     self.diff = len(self.args)-len(other.args)
        #     for x in range(0,self.diff):
        #         self.result.append(int(self.args[x])-int(other.args[x]))
        #     for x in range(self.diff-1, len(self.args)):
        #         self.result.append(0)

funkcja1 = Function("1*x**2+5*x+5")
print(funkcja1.calculate(1)) # 11

funkcja2 = Function("1*x**4+2*x+2")
print(funkcja2.calculate(1)) # 5