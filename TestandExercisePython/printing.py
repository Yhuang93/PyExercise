class Test:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __repr__(self):
        return "Test a :%s,b:%s" %(self.a,self.b)
    def __str__(self):
        return "Str method:%s%s" %(self.a,self.b)

T=Test("huang","yining")
print(T)
