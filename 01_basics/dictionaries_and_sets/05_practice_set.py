# Question 1

set1 = set()
E1 = input("Enter a number : ")
set1.add(E1)
E2 = input("Enter a number : ")
set1.add(E2)
E3 = input("Enter a number : ")
set1.add(E3)
E4 = input("Enter a number : ")
set1.add(E4)
E5 = input("Enter a number : ")
set1.add(E5)
E6 = input("Enter a number : ")
set1.add(E6)

print("Unique numbers are : ", set1)

# Question 2

s = set()
s.add(20)
s.add(20.0)            # 20.0 == 20
s.add('20')
print(f"Length of set s : {s} after given add() operations is {len(s)} ")

# Question 3

dictionary = {}

n1 = input("Enter your name ")
l1 = input("Enter your favourite language ")
dictionary.update({n1 : l1})

n2 = input("Enter your name ")
l2 = input("Enter your favourite language ")
dictionary.update({n2 : l2})

n3 = input("Enter your name ")
l3 = input("Enter your favourite language ")
dictionary.update({n3 : l3})

n4 = input("Enter your name ")
l4 = input("Enter your favourite language ")
dictionary.update({n4 : l4})

print(dictionary)