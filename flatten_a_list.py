def flatten(list2):
    listTemp = []
    for item in list2:
        for i in item:
            listTemp.append(i)
    return listTemp

print(flatten([[1, 2], [3, 4]]))