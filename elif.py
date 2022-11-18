# task1

"""num = int(input("Enter a number: "))
if num == 10:
    print("Number is 10")
elif num == 20:
    print("Number is 20")
elif num == 30:
    print("Number is 30")
    
else :
    print("number is not 10, 20 or 30")"""


# task 2
marks = int(input("Enter the marks :  "))
if marks > 85 and marks <= 100:
    print("Congrats ! you scored grade A ...")
elif marks > 60 and marks <= 85:
    print("You scored grade B ...")
elif marks > 40 and marks <= 60:
    print("You scored grade C ...")
elif (marks > 30 and marks <= 40):
    print("You scored grade D ...")
else:
    print("Sorry you are fail.!")
