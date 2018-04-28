# Function with *args and calling the function with list
def Add_together(*args):
    total=0
    for arg in args:
        total+=int(arg)
    print(total)
    return
lst=(1,2,3,4,5,6,7,8,9)
Add_together(lst)
     #print(type(arg))
#lst=[1,2,3,4,5,6,7,8,9]
#Add_together(lst)
        
