# Raising Exception
try:
    a=2
    if a<4:
        b=a/(a-3)
        raise NameError("Hi there")
except ZeroDivisionError:
                    print("An exception")
                
                
