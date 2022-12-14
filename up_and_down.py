def number(number):
    list1 = []
    down = number - 1
    list1.append(down)
    up = number + 1
    list1.append(up)
    tupleNumber = tuple(list1)
    return tupleNumber


print(number(101))
