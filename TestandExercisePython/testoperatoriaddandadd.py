#try to find the difference between add() and iadd() under the operator module
import operator
def using_add_to_add_two_lists(lst_1,lst_2):
    lst_3=operator.add(lst_1,lst_2)
    print(lst_3)
    return lst_3
