# Να διορθωθούν τα λάθη στον παρακάτω κώδικα και να εξηγηθεί η λειτουργία του

string = input("Enter a string: ")
reverse = ""

for i in string:
    reverse = i + reverse

    if string == reverse:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")