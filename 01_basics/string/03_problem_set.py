# Question 1
name = input("Enter name : ")
print("Good Afternoon ", name)

# Question 2
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>", name).replace("<|Date|>", "14 July, 2026"))

# Question 3
str1 = input("Enter a string to detect double whitespace : ")
print(str1.find("  "))


# Question 4
print(str1.replace("  ", " "))


# Question 5
letter2 = "Hey user,\n\tthis is python practice program.\nThanks!"
print(letter2)