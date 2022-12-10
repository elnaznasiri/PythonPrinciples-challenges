# solution 1
def add_dots(str):
    jointString = ".".join(str)
    return jointString

def remove_dots(str):
    splitString = str.split(".")
    joinString = "".join(splitString)
    return joinString

print(remove_dots(add_dots("test")))


# solution 2
def add_dots(str):
    temp = ""
    for letter in str:
        temp += letter + "."
    return temp[:-1]

def remove_dots(str):
    return str.replace(".", "")

print(remove_dots(add_dots("test")))