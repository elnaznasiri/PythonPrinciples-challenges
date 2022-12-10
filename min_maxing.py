# solution 1
def largest_difference(list1):
    for item in list1:
        maxNumber=max(list1)
        minNumber=min(list1)
    return maxNumber-minNumber
    
print(largest_difference([1, 2, 3]))


# solution 2
def largest_difference(list1):
    list1.sort()
    minList = list1[0]
    maxList = list1[-1]
    return maxList - minList

print(largest_difference([5,8,9,12,1]))
