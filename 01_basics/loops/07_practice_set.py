# Question 1
n = int(input("Enter a number : "))
for i in range(1,11):
    print(f" {n} x {i} = {n*i} ")

# Question 2

l = ["Harry", "Soham", "Sachin", "Rahul"]
for name in l:
    if(name.startswith("S")):
        print("Hello, ", name)

# Question 3

n1 = int(input("Enter a number : "))
for j in range(2,n1):
    if(n1%j == 0):
        print("Number is not prime")
        break
else:
    print("Number is prime")

# Question 4

n2 = int(input("Enter a number : "))
a=1
sum=0
while(a<(n2+1)):
    sum+=a
    a+=1

print(f"Sum of first {n2} natural numbers is {sum}")

# Question 5

n3 = int(input("Enter a number : "))
b=1
fact=1
while(b<(n3+1)):
    fact*=b
    b+=1

print(f"Sum of first {n3} natural numbers is {fact}")

# Question 6 

n4 = int(input("Enter a number : "))
for star in range(1, (n4+1)):
    print(" "*(n4-star), end="")
    print("*"*(2*star-1), end="") 
    print("")

# Question 7

n5 = int(input("Enter a number : "))
for stars in range(1, (n5+1)):
    print("*"*(stars), end="") 
    print("")

# Question 8

n5 = int(input("Enter a number : "))
for box in range(1, (n5+1)):

    if(box==1 or box==n5):
        print("*"*n5, end="")
    else:
        print("*", end="")
        print(" "*(n5-2), end="")
        print("*", end="")    
    print("")