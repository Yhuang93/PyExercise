#comparison between add and iadd
import operator
lst_1=[1,2,3,4]
lst_2=[90,98]
lst_3=operator.add(lst_1,lst_2)
print(lst_3)
print(lst_1)
lst_4=[5,6,7,8]
lst_5=[121,234]
lst_6=operator.iadd(lst_4,lst_5)
print(lst_6)
print(lst_4)
