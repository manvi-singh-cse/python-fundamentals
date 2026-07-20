list1 : list[int] = [1, 2, 3, 4, 5]                                   # list is int data-type (similar for tuple, dict, union)
numbers : list[int] = [1, 2, 3] 
person : list[int, str] = ["Manvi", 20, "Alice", 25]                  # list is of both str and int data-type

# without walrus 
n = len(list1)
if(n>3):
    print(f"Too long list with {n} elements")
else:
    print(f"List length is {n}")

# with walrus 
if(i := len(numbers)) > 3:
    print(f"Too long list with {i} elements")
else:
    print(f"List length is {i}")



a : int = int(input("Enter number 1 "))                               # int data-type vaiable
b : int  = int(input("Enter number 2 "))                              # int data-type vaiable
operation : str = input("Choose operation among add/sub/mul/div ")    # str data-type vaiable

def Calculator(operation : str) -> str :                              # both parameters and return value is str data-type
    match operation:                                                  # match-case 
        case "add":
            return (f"Sum of {a} and {b} is {a+b}")
            
        case "sub":
            return (f"Difference of {a} and {b} is {a-b}")

        case "mul":
            return (f"Product of {a} and {b} is {a*b}")

        case "div":
            return (f"Quotient on divinding {a} by {b} is {a/b}")

print(Calculator(operation))