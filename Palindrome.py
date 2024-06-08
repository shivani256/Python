def is_palindrome_string(s):
    return s == s[::-1]

string = input("String: ")
if is_palindrome_string(string):
    print("Palindrome")
else:
    print("Not a Palindrome")
