# Python program to find if  a string is palindrome 
def is_palindrome(string):
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    return cleaned_string == cleaned_string[::-1]

string = input("Enter a string:")

if is_palindrome(string):
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')
