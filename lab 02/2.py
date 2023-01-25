x1, y1 = eval(input("Enter the x1, y1 : "))
x2, y2 = eval(input("Enter the x1, y1 : "))
x3, y3 = eval(input("Enter the x1, y1 : "))

area = (1/2) * (x1*(y2-y3) + x2 * (y3-y1) + x3 * (y1-y2))
print("Area of triangle : ", area);