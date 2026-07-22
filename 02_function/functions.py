# Function is block of code/statement to perform a particular task

def avg():                                         # Function definition 
    a = int(input("Enter first number "))
    b = int(input("Enter second number "))

    return ((a+b)/2)                               # return statement sends back value/object to user

average = avg()                                    # function call
print("Average is ", average)

def greet(name = "Guest"):                         # default parameter
    print ("Hello, ", name)

greet("Manvi")                                     # function call with argument
greet() 