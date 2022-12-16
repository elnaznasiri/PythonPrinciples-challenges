def all_equal(list1):
    result = all(element == list1[0] for element in list1)
    if (result):
        return True
    else:
        return False
print(all_equal([1, 1, 1]))