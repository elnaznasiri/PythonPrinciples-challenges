# solution 1
def largest_difference(list1):
    for item in list1:
        maxNumber=max(list1)
        minNumber=min(list1)
    return maxNumber-minNumber
print(largest_difference([1, 2, 3]))
