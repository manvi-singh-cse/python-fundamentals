marks = {                       # Mutable and no-duplicate
    "manvi" : 96,
    "bhavesh" : 92,
    "devang" : 78,
    "palak" : 89,
}

empty_dict = {}

print("Marks are : ",marks)
print("Marks of 'manvi' are : ", marks["manvi"])

# Dictionary Methods

print("Length of 'marks' dictionary is : ", len(marks))

print("Items of 'marks' dictionary are : ", marks.items())

print("Keys of 'marks' dictionary are : ", marks.keys())

print("Values of 'marks' dictionary are : ", marks.values())

print("Marks of 'manvi' are : ", marks.get("manvi"))

marks.update({"palak" : 90})
print("Updated marks of 'palak' are : ", marks.get("palak"))

marks.update({"shloka" : 97})                                   # add field if not present 
print("Marks of 'shloka' are : ", marks.get("shloka"))
print("Updated marks dictionary is : ",marks)

copy1 = marks.copy()
print("Shallow copy of  'marks' dictionary is : ", copy1)

print("Popped item of 'marks' is (using pop) : ", marks.pop("bhavesh", "default"))

print("Popped item of 'marks' is (using pop) : ", marks.pop("priya", "Not Found key - default"))

print("Popped item of 'marks' is (using popItem) : ", marks.popitem())

marks.clear()
print("?Now 'marks' dictionary is : ", marks)