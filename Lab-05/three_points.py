class points:
    def __init__(self, x1, x2, x3, y1, y2, y3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3

    def calculate(self):
        return float(0.5 * (self.x1 * (self.y2 - self.y3) + self.x2 * (self.y3 - self.y1) + self.x3 * (self.y1- self.y2)))

x1, y1 = eval(input("Enter x1, x2: "))
x2, y2 = eval(input("Enter x2, y2: "))
x3, y3 = eval(input("Enter x3, y3: "))

obj = points (x1, x2, x3, y1, y2, y3)
print(obj.calculate())
