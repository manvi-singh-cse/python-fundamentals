string1 = "manvi"
string2 = ''' singh'''

print("Length of string1 is ", len(string1))
print("Does string1 ends with h? ", string1.endswith("h"))
print("Does string1 starts with m? ", string1.startswith("m"))
print("Capitalized string1 is ", string1.capitalize())
print("Uppercase string1 is ", string1.upper())
print("Lowercase string1 is ", string1.lower())

name = string1 + string2

print("Title of name ", name.title())
print("Name has an at index? ", name.find("an"))
print("Replace string1 with bhavesh ", name.replace("manvi", "bhavesh"))