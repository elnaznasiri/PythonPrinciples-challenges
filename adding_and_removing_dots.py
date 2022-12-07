def add_dots(str):
    jointString = ".".join(str)
    return jointString

def remove_dots(str):
    splitString = str.split(".")
    joinString = "".join(splitString)
    return joinString

print(remove_dots(add_dots("test")))
