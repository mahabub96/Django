

def is_palindrome(s):
    # Convert the entire string to lowercase
    s = s.lower()
    # Check for palindrome
    return s == s[::-1]

#Taking input
string=input("Enter a valid string: ")
#showing output
print(f"the string is palindrome: {is_palindrome(string)}")