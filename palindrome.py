# solution 1
def palindrome(string):
    if(string==string[::-1]):
        print("The string is a palindrome")
        return True
    else:
        print("Not a palindrome")
        return False


string = input("Enter string: ")
palindrome(string)


# solution 2
def palindrome(string):
    lenght=len(string)
    i=0
    j=lenght-1
    flag=True
    while(i<j):
        if string[i]!=string[j]:
            flag=False
            break
        i+=1
        j-=1

    if flag==True:
        return("Yes")
    else:
        return("No")

string = input("Enter string: ")
print(palindrome(string))