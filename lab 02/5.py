number = eval(input("Enter number : "))

for x in range (2, 100):
    y = number % x;
    if y == 0:
        print("smallest factor : ", number, "is ", x)
        break