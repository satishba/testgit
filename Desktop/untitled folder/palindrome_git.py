def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

stringz = input("Enter a string: ")
if is_palindrome(stringz):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
