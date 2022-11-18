"""# multi table
n = int(input("Enter the number "))
for i in range(1, 11):
    c = n*i
    print(n, "*", i, "=", c)"""

"""# reverse
num = 1234
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number : " + str(reversed_num))"""


# sum of digits
sum = 0
num = int(input("Enter a number: "))
while (num > 0):
    x = num % 10
    sum = sum + x
    num = num // 10
print("Sum of digits of the number is: ", sum)
