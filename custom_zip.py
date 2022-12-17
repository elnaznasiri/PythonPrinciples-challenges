def zap(a, b):
    result = []
    for i in range(len(a)) :
        tuple_result = (a[i],b[i])
        result.append(tuple_result)
    return result

print(zap(
    [0, 1, 2, 3],
    [5, 6, 7, 8]
))
