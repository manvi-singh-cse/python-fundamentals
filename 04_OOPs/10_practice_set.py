# Question 1

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"Square of {self.n} is {self.n**2}")

    def cube(self):
        print(f"Square of {self.n} is {self.n**3}")

    def square_root(self):
        print(f"Square of {self.n} is {self.n**(1/2)}")

a = Calculator(4)
a.square()
a.cube()
a.square_root()

# Question 2

class Demo:
    class_attribute = 52

b = Demo()
b.class_attribute = 23
print(b.class_attribute)
print(Demo.class_attribute)       # class attribute is not changed, instead instance attribute is set and displayed in above line.

# Question 3

class Manvi:
    name = "Manvi"

    def intro(self):
        print(self.name)

    def info(manvi):
        print(manvi.name)

myself = Manvi()
myself.intro()
myself.info()