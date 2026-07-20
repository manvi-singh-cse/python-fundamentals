# enumerate , list comprehension , lambda , format , join 

fruit = ["Mango", "Banana", "Guava", "Apple"]
numbers = [2, 4, 7, 9, 12]

for index, item in enumerate(fruit):                               # gets both iterated item and it's index with no extra code
    print(f"{item} fruit is on index {index}")

squared = [n**2 for n in numbers]                                  # list comprehension : new list from existing list in 1-line code
print("Squared list is ", squared)

x = int(input("Enter number to get it's cube "))
cube = lambda n : n**3                                             # creates un-named single line function
print("Cube of {} is {}".format(x, cube(x)))                       # older way of formatting strings

print("First {1} in list is {0}".format(fruit[0], "fruit") )       # default is {0} then {1} 

fruits = "-".join(fruit)                                           # merges list of strings into one using a separator
print("Fruit chain is ", fruits)