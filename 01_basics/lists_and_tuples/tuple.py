tuple1 = (3, 1, 8, 0, 2, 9)       # Immutable
tuple2 = (12, )          # Single value tuple initialization 

print("Tuple 1 is : ", tuple1)

# Tuple Methods 

print("Length of Tuple 1 is : ", len(tuple1))

print("Index of \"0\" is : ", tuple1.index(0))

print("Count of 31.8 in Tuple 1 is : ",tuple1.count(31.8))

print("Tuple 1 containes 31.8? ", tuple1.__contains__(31.8))

print("Tuple 1 containes 3? ", 3 in tuple1)

print("Minimum in tuple 1 is : ", min(tuple1))

print("Maximum in tuple 1 is : ", max(tuple1))

print("Sum of tuple 1 is : ", sum(tuple1))

print("Tuple 2 is : ", tuple2)

print("Tuple 2 printed 3 times ", tuple2*3)

print ("tuple 1 and Tuple 2 combined is : ", tuple1+tuple2)

a, b, c, d, e, f = tuple1

print(f"Destructured Tuple 1 is, a : {a} , b : {b} , c : {c} , d : {d} , e : {e} , f : {f} ")