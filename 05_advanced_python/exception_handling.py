try:
    a = int(input("Enter number 1 "))
    b = int(input("Enter number 2 "))

    if(a>200 or b>200 or a<0 or b<0):
        raise ValueError("Numbers should be in range (0,201) both exclusive")

    quotient = a/b 

    print(f"Quotient on divinding {a} by {b} is {quotient}")

except ZeroDivisionError as v:
    print("This program is not made to handle division by 0")

except Exception as e:
    print(e)

finally:
    print("Thank you!")