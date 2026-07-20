counter = 0 

print("Initial value of global counter ", counter)

def update_global_counter():
    global counter                                          # access and change value of global variable
    counter = 10
    print("Counter value in update_global_counter() is ", counter)


def update_local_counter():
    counter = 15                                            # do not change value of global variable
    print("Counter value in update_local_counter() is ", counter)

update_global_counter()
update_local_counter()

print("Global Counter value at end of program is ", counter)     