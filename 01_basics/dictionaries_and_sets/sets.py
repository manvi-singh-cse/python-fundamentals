set1 = {1, 2, 5, 4, 6, 7}      # Unordered, Unindexed, collection of non-repetitive elements
set2 = set()

print("Set 1 is : ", set1)
print("Set 2 is : ", set2)

# Set Methods 

print("Length of set 1 is : ", len(set1))

set2.add(11)
print("New set 2 is (after add(11)) : ", set2)

s1_copy = set1.copy()
print("Copy set 1 is : ", s1_copy)

set1.discard(4)
print("New set 1 is (after discard(4)) : ", set1)

set1.pop()
print("New set 1 is (after pop()) : ", set1)

set1.remove(6)
print("New set 1 is (after remove(6)) : ", set1)


print("Union of set1 and set2 is : ", set1.union(set2))

print("Intersection of set1 and set2 is : ", set1.intersection(set2))

print("Difference of set1 and set2 is : ", set1.difference(set2))
print("Difference of set2 and set1 is : ", set2.difference(set1))

set1.clear()
print("New set 1 is (after clear()) : ", set1)