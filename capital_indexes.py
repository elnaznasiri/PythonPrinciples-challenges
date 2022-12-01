def capital_indexes(arg):
    MyList = []
    for i, item in enumerate(arg):
        if item == item.capitalize():
           MyList.append(i)
    return MyList

print(capital_indexes("HeLlO"))