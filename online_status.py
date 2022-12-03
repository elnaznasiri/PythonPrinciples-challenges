# solution 1
def online_count(arg):
    count = 0
    for i in arg:
        if arg[i] == "online":
            count +=1
    return count


# solution 2
def online_count(dic):
    count= 0
    for value in dic.values():
        if value == "online":
            count +=1
    return count

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
print(online_count(statuses))