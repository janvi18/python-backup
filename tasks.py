"""# multi table

n = int(input("Enter the number "))
for i in range(1, 11):
    c = n*i
    print(n, "*", i, "=", c)
"""

# reverse
num = 1234
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number : " + str(reversed_num))
