from functools import reduce

five_natural_numbers = [1, 2, 3, 4, 5]

square = lambda n : n**2
sum = lambda a,b : a+b 

def even(n):
    if(n%2 == 0):
        return True
    return False

squared_list = map(square, five_natural_numbers)
print(list(squared_list))
# Other way for Map : 
# squared = list(map(lambda n : n**2, five_natural_numbers))
# print(squared)

even_list = filter(even, five_natural_numbers)
print(list(even_list))
# Other way for Filter : 
# even_list = list(filter(lambda a : a%2==0, five_natural_numbers))
# print(even_list)

reduced_sum = reduce(sum, five_natural_numbers)
print(reduced_sum)
# Other way for Reduce : 
# reduced = int(reduce(lambda x,y : x+y, five_natural_numbers))
# print(reduced)