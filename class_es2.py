class IntPair:
    def __init__(self,a=1,b=1):
        self.a=a
        self.b=b
    
    def __str__(self):
        return "ip(%d,%d)" % (self.a,self.b)
    
    def mul(self):
        return self.a*self.b

n1=IntPair()
print(n1.__str__(),n1.mul())

n2=IntPair(4,3)
print(n2.__str__(),n2.mul())