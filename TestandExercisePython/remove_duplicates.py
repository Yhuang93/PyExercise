def remove_duplicates(lst):
    new_lst=[]
    new_lst.append(lst[0])
    lst.sort()
    for i in range(1,len(lst)):
        if lst[i] != lst[i-1]:
            new_lst.append(lst[i])
    print(new_lst)
    return new_lst
            
