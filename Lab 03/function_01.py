def sort(number1, number2):
    if number1<number2:
        return number1,number2
    else:
        return number2,number1


n1, n2 = sort(5,4)
print("n1 is : ", n1)
print("n2 is: ", n2)

def f(x,y):
    return x+y, x-y, x*y, x/y

t1, t2, t3,t4 = f(5,4)
print(t1, t2, t3, t4)
