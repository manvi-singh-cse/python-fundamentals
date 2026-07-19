class Number:
    def __init__(self, n):
        self.number = n

    def __add__(self, num):
        if(type(num) == Number):
            add_value = num.number
        else:
            add_value = num
        return Number(self.number + add_value)
    
    def __sub__(self, num):
        if(type(num) == Number):
            sub_value = num.number
        else:
            sub_value = num
        return Number(self.number - sub_value)
    
    def __str__(self):
        return str(self.number)

a = Number(1)
b = Number(2)
c = Number(5)
d = Number(4)

sum = a+b
print(sum)
print(c-sum)
print(c-d)