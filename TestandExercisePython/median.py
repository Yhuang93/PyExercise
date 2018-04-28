def median(lst):
    new_lst=sorted(lst)
    lenew=len(new_lst)
    if lenew % 2 == 0:
        index_1 = int((lenew/2)-1)
        index_2 = int(lenew/2)
        med=((new_lst[index_1]) + (new_lst[index_2]))/2
    elif lenew % 2 != 0:
        index_1 = lenew-1
        index_2 = int(index_1 * 0.5)
        med = new_lst[index_2]
    return med
