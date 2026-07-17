for i in range(1, 11 ):                             # range(11) = range(0, 11)
    print(i)

for j in range(1, 11, 2 ):                          # format is range(start, stop, step_size)
    print(j)

list1 = ["q", "w", "e", "r", "t", "y"]              # for loop on list (similar for strings, tuples, etc)
for item in list1:
    print(item)
else:                                               # for loop with 'else'
    print("Done")                                   # runs after loop ends 

for a in range(20):
    pass                                              # do nothing for now. Otherwise it gives error for leaving loop empty. 

for b in range(20): 
    if(b == 3):
        continue                                      # 'continue' skips the iteration if condition satisfies
    if(b == 8):
        break                                         # 'break' exits the loop if condition satisfies
    print(b)