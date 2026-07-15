# Question 1

M1 = int(input("Enter marks of subject 1 "))
M2 = int(input("Enter marks of subject 2 "))
M3 = int(input("Enter marks of subject 3 "))
M4 = int(input("Enter marks of subject 4 "))

if(M1>M2 and M1>M3 and M1>M4):
    print(f"Marks of subject 1, {M1} is maximum")
elif(M2>M1 and M2>M3 and M2>M4):
    print(f"Marks of subject 2, {M2} is maximum")
elif(M3>M1 and M3>M2 and M3>M4):
    print(f"Marks of subject 3, {M3} is maximum")
elif(M4>M1 and M4>M3 and M4>M2):
    print(f"Marks of subject 4, {M4} is maximum")

# Question 2

per = ((M1+M2+M3+M4)*100)/400

if(per>40 and M1>33 and M2>33 and M3>33 and M4>33): 
    print(f"Student has passed with {per} total percentage")

# Question 3

msg = input("Enter message ")
if("Make a lot of money" in msg or "buy now" in msg or "click this" in msg): 
    print("Message is spam")
else:
    print("Message is not spam")