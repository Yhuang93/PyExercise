class X(object):
    def __init__(self,a):
        self.num = a
    def doubleup(self):
        self.b=self.num*2
 
class Y(X):
    def __init__(self,a):
        X.__init__(self, a)
        #X.num=a
    def tripleup(self):
        self.num *= 3
 
obj = Y(4)
print(obj.num)
 
obj.doubleup()
print(obj.b)
 
obj.tripleup()
print(obj.num)
