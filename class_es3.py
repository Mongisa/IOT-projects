class IntPair:
    def __init__(self,a=1,b=1):
        self.a=a
        self.b=b
    
    def __str__(self):
        return "ip(%d,%d)" % (self.a,self.b)
    
    def mul(self):
        return self.a*self.b

class IntPairK(IntPair):
    def __init__(self, a=1, b=1, k=1):
        super().__init__(a*k, b*k)

    #Override
    def __str__(self):
        return "ipk(%d,%d)" % (self.a,self.b)

n1=IntPairK(3,2,3)
print(n1.__str__(), n1.mul())