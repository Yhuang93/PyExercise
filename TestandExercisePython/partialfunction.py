import functools
def add(a,b,c):
    return 100*a+10*b+c
add_part=functools.partial(add,c=3)
print(add_part(2,1))
