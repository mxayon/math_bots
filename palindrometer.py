## Palindrometer - Find out if word is a Palindrome

## Palindrome Tests:
##

def isPalindrome(str):
    #reverse string input
    reverse = ''.join(reversed(str))

    #checks if strings are equal
    if (str == reverse):
        return True
    return False

str = input('Please Enter what you think may be a palindrome')
str = str.casefold()
answer = isPalindrome(str)

if (answer):
    print("Yes you caught a Palindrome")
else:
    print("Nope, not a palindrome")
