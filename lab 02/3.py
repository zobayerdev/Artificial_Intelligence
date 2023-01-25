height = float(input("Enter your height in (inches): "))
weight = float(input("Enter your wight in pounds: "))

h = float(height * 0.0254)
w = float(weight * 0.45359237)

BMI = w / float(h*h)

if BMI < 18.5:
    print("Underweight");
elif BMI > 18.5 and BMI <= 24.9:
        print("Normal")
elif BMI > 25.0 and BMI <= 29.9:
        print('Overweight')
elif BMI > 30.0:
        print('Obesity')
else:
    print("Motu")

