# Question 1

marks = []

M1 = input("Enter marks of student 1 : ")
marks.append(M1)
M2 = input("Enter marks of student 2 : ")
marks.append(M2)
M3 = input("Enter marks of student 3 : ")
marks.append(M3)
M4 = input("Enter marks of student 4 : ")
marks.append(M4)
M5 = input("Enter marks of student 5 : ")
marks.append(M5)
M6 = input("Enter marks of student 6 : ")
marks.append(M6)
M7 = input("Enter marks of student 7 : ")
marks.append(M7)

print("Entered marks in list are : ", marks)

# Question 2

marks.sort()
print("Sorted marks are : ", marks)

# Question 3

numbers = [74, 52, 42, 77]
print("Sum of numbers list is : ", sum(numbers))

# Question 4

tuple1 = (7, 0, 8, 0, 0, 9)
print("Number of '0' in given tuple are : ", tuple1.count(0))