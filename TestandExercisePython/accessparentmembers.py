class Base(object):
 
    # Constructor
    def __init__(self, x):
        self.x = x    
 
class Derived(Base):
 
    # Constructor
    def __init__(self, x):
        Base.x = x 
        
 
    def printXY(self,y):
        self.y=y
       # print(self.x, self.y) will also work
        print(Base.x, self.y)
    def printX(self):
        print (Base.x)
 
 
# Driver Code
d = Derived(10)
d.printX()
