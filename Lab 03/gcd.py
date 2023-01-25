def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Enter First Integer Number: "))
num2 = int(input("Enter Second Integer Number:  "))
print("The greatest common divisor of", num1,"and", num2,"is", gcd(num1, num2))
