def count(str):
    syllables = 1
    for item in str:
        if item == "-":
            syllables += 1
    return syllables

print(count("ter-min-a-tor"))
