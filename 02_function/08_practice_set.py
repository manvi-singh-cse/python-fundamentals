# Question 1

def greatest():
    a = int(input("Enter first number "))
    b = int(input("Enter second number "))
    c = int(input("Enter third number "))
    
    if(a>b and a>c):
        print("First number is greatest")
    elif(b>a and b>c):
        print("Second number is greatest") 
    elif(c>a and c>b):
        print("third number is greatest")

greatest()

# Question 2

print("Doesn't give a new line", end="")                         # end="" doesn't give a new line
print("_New line begins here")

# Question 3

def sum(n):
    if(n==0):
        return 0
    return n + sum(n-1)

n = int(input("Enter the number "))
sum_value = sum(n)
print(f"Sum of {n} natural numbers is {sum_value}")

# Question 4

def pattern(lines = 3):
    i=lines
    while(i<(lines+1) and i>0):
        print("*"*i, end="")
        print("")
        i -= 1

n1 = int(input("Enter the number of lines for pattern "))
pattern(n1) 