marks = int(input("Enter your marks "))

if(marks>90 and marks<100) :                       # Can have multiple 'if' statements too
    print("Your grade is \"Excellent\"")
elif(marks>80 and marks<90) :
    print("Your grade is \"A\"")
elif(marks>70 and marks<80) :
    print("Your grade is \"B\"")
elif(marks>60 and marks<70) :
    print("Your grade is \"C\"")
elif(marks>50 and marks<60) :
    print("Your grade is \"D\"")
else :
    print("Your grade is \"F\"")