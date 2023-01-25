def isValid(side1, side2, side3):
    sum = side1 + side2 + side3
    if sum == 180 and side1 != 0 and side2 != 0 and side3 != 0:
        return True
    else:
        return False


def area(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    return (s * (s-side1) * (s - side2) * (s - side3)) ** 0.5


side1 = int(input("1st "))
side2 = int(input("2nd "))
side3 = int(input("3rd "))

if isValid(side1, side2, side3):
    print("Triangle Area ", area(side1, side2, side3))
else:
    print("Invalid Input")