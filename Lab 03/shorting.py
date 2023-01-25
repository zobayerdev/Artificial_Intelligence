def displaySortedNumbers(num1, num2, num3, num4):
    numbers = [num1, num2, num3, num4]
    numbers.sort()
    for num in numbers:
        print(num)


num1, num2, num3, num4 = input("Enter three numbers separated by space: ").split()
num1, num2, num3, num4 = int(num1), int(num2), int(num3), int(num4)
displaySortedNumbers(num1, num2, num3,  num4)
