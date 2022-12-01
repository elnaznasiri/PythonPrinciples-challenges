# solution 1
def mid(str):
    if len(str) % 2 == 1:
        i = len(str)//2
        return str[i]
    return ""
print(mid("abcd"))


# solution 2
def mid(str):
    if len(str) % 2 == 0:
        return ""
    else:
        return str[len(str)//2]

print(mid("abc"))


