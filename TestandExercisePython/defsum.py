def digit_sum(n):
    right1 = n % 10
    i = 1
    a = 0
    sum = 0
    after_get_rid_right = n // 10 ** 1
    final_list=[]
    final_list.append(right1)
    while after_get_rid_right >=1:
        right1= after_get_rid_right % 10
        final_list.append(right1)
        
        after_get_rid_right = after_get_rid_right // 10 ** 1
        
    print (final_list)
    for item in final_list:
        sum += item
    return sum
