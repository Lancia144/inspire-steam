# Nmae : Daniel nduati
# date : 16/02/2026
# program to calculate factorials of number

number = int(input("enter the number x : "))

factorial = 1 # intiate factorial
for x in range (1,number):
    factorial = (number) * (number+1)
    factorial *= x
print(f"{number}! = {factorial}")