def reverse(number):
    rev = 0
    while number > 0:
        digit = number % 10
        rev = (rev * 10) + digit
        number = number // 10
    return rev

def isPalindrome(number):
    return number == reverse(number)


num = int(input("Enter an integer: "))
if isPalindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
