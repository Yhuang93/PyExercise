def Generator1():
    yield 1
    yield 2
    yield 3
x= Generator1()
print(x.__next__())
print(x.next())
print(x.__next__())
