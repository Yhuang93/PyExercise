# Practice：using decorate to add some string to
# a function that returns a number
def To_decorate(somefunc):
    def add_some_string(a,b):
        print("If you put two numbers in this decorate:",somefunc(a,b))
        temp=somefunc(a,b)
        return temp
    return add_some_string
        

@To_decorate
def summation_together(a,b):
    return a+b

print (summation_together(2,3))
