#编写coroutine时候，要用yield来接受输入，调用定义的函数（coroutine）并赋值给一个变量时不会发生什么

#之后要调用变量.__next__()来开始执行coroutine

#接受输入要使用变量.send（）
def print_number_somenum(num):
    print("We are printing the number {}.".format(num))
    while True:
        lst=(yield)
        if num in lst:
            print(lst)
    # yield
    
corou=print_number_somenum(2)
corou.__next__()
corou.send([2,3,4])
corou.send([3,4])
corou.send([1,2,3])

