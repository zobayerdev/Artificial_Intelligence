def sumofdigit(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number = number // 10
    return sum
num = eval("Enter The Some Number : ")
print('sum of digit: ', sumofdigit(num))