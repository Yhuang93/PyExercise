class X(object):
    def __init__(self,a):
        self.a = a
    def doubleup(self):
        self.a *= 2
 
class Y(X):
    def __init__(self,a):
        X.a=a
    def tripleup(self):
        X.a *= 3
 
obj = Y(4)
print(obj.a)
 
obj.doubleup()
print(obj.a)
 
obj.tripleup()
print(obj.a)
