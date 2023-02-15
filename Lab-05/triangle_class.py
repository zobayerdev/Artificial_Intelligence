class triangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height
        print("Destroy")


    def show(self):
        return 0.5 * self.base * self.height

obj = triangle(15, 20)
print(obj.show())
del obj