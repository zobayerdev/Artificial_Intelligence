class BMI:
    def __init__(self, name, age, weight, height):
        self.bmi = 0
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def calculatebmi(self):
        A1 = float(self.weight * 0.45359237)
        A2 = float(self.height + 0.0254)
        return A1/float(A2*A2)

    def status(self):
        if self.calculatebmi() <= 18.5:
            return "Underweight"
        elif 18.5 < self.calculatebmi() <=24.5:
            return "Your weight is normal"
        elif 24.5 < self.calculatebmi() <= 29.29:
            return "You are overweight"
        else:
            return "Obese"

name = input("Enter your name: ")
age = input("Enter your age: ")
weight = eval(input("Enter your weight: "))
height = eval(input("Enter your height: "))

obj = BMI(name, age, weight, height)
print(obj.status())