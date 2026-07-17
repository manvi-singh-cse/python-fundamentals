i=1 
while(i<11):                             # while loop
    print(i)
    i+=1

j=1 
while(j<11):                             # while loop with step_size=2
    print(j)
    j+=2                                 # step_size=2

list1 = [1, 4, 6, 2, 7]                  # while loop on list
k=0 
while(k<len(list1)):
    print(list1[k])
    k+=1

a=0
while a in range(20): 
    if(a == 8):
        break                                         # 'break' exits the loop if condition satisfies
    print(a)
    a+=1