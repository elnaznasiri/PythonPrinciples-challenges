def palindrome(string):
    if(string==string[::-1]):
        print("The string is a palindrome")
        return True
    else:
        print("Not a palindrome")
        return False


string = input("Enter string: ")
palindrome(string)