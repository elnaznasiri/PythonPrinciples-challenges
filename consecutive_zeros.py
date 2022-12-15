def consecutive_zeros(str):
    list1 = []
    c = 0
    maximumZero = 0
    for i in str:
        i = int(i)
        if i<1:
            c+=1
            list1.append(c)
            maximumZero = max(list1)
        else:
            c = 0
    return maximumZero
print(consecutive_zeros("1001101000110"))

