def online_count(arg):
    count = 0
    for i in arg:
        if arg[i] == "online":
            count +=1
    return count



statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
print(online_count(statuses))