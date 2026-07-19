# Question 1 

class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"The 2-D vector is {self.i}i + {self.j}j ")
        

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The 3-D vector is {self.i}i + {self.j}j + {self.k}k")

a = TwoDVector(1, 2)
a.show()
b = ThreeDVector(5, 2, 3)
b.show()

# Question 2

class Employee:
    salary = 60000
    increment = 15

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment =  ((salary/self.salary) -1)*100

manvi = Employee()
print("Salary of the employee is ", manvi.salary)
print("Increment percentage for employee is ", manvi.increment)
print("Salary after increment is ", manvi.salaryAfterIncrement)

print("Setting new salary using setter ... ")
manvi.salaryAfterIncrement = 70000
print("New salary is ", manvi.salaryAfterIncrement)

# Question 3

class Complex:

    def __init__(self, real, imaginary):
        self.real = real 
        self.img = imaginary 
    
    def __add__(self, num):
        return Complex(self.real + num.real , self.img + num.img)

    def __sub__(self, num):
        return Complex(self.real - num.real , self.img - num.img)

    def __str__(self):
        sign = "+" if self.img >= 0 else "-"
        return f"{self.real} {sign} {abs(self.img)}i"
    
c1 = Complex(1, 2)
c2 = Complex(3, 4)
print("Complex number 1 is ", c1)
print("Complex number 2 is ", c2)
print("Sum of both complex numbers is ", c1 + c2)
print("Difference of both complex numbers is ", c1-c2)