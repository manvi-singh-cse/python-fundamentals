''' 
A file is data stored in a storage device. The random-access memory is volatile, and all its contents are lost once a program terminates. In order to
persist the data forever, we use files. 
'''

file1 = open("file1.txt", "r")                        # open file1 in read mode 
data = file1.read()
print(data)
file1.close()


file01 = open("file1.txt", "a")                       # open file1 in append mode 
file01.write("\n Latest Appended Text :- \n "
            "Line1 \n " \
            "Line2 \n " \
            "Line3 ")
file01.close()


file02 = open("file1.txt", "r")
lines = file02.readlines()                            # using readlines() to get list of lines in file
for text in lines:
    print(text)
file02.close()

'''
content = file02.readline()
print(content)
content2 = file02.readline()
print(content2)
content3 = file02.readline()
print(content3)
content4 = file02.readline()
print(content4)
'''


with open("file2.txt", "w") as file2 :                # open file2 in write mode using 'with'
    file2.write("Text entered. \n")
    with open("file1.txt", "r") as file:
        content = file.read()
        file2.write(content)