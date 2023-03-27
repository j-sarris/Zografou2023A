string = input("Enter a string: ")

for i in string:
    reverse = i + reverse

    if string == reverse:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
