list1 = ["apple", "mango", "banana", 20, True]          # MUTUABLE
list2 = [3, 10, 4, 5]

print("List 1 is : " ,list1)
print("List 2 is : " ,list2)
print(list1[2])
print(list1[2:])  # Same as print(list1[2:5])

# List Methods 
list2.sort()
print("New List 2 is (after sort()) : " ,list2)

list1.append(31.8)
print("New List 1 is (after append()) : " ,list1)

list1.insert(2, 12)
print("New List 1 is (after insert()) : " ,list1)

print("Length of list 1 is : ", len(list1))

print("Popped element is : ",list1.pop(3))

list1.remove(20)
print("New List 1 is (after remove()) : " ,list1)

list1.reverse()
print("New List 1 is (after reverse()) : " ,list1)


print("Count of 31.8 in List 1 is : ",list1.count(31.8))


print("List 1 containes 31.8? ", list1.__contains__(31.8))

list1.clear()
print("Now List 1 after clear() is : ", list1)