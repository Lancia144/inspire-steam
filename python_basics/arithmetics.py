# Nmae : Daniel nduati
# date : 17/02/2026
# Program to perform arithmetic opertions

f_number = 12
s_number = 34
sum_number = f_number  + s_number
diff_number = f_number  - s_number
product_number = f_number  * s_number
quotient_number = f_number  / s_number


print("the sum of the number %d" %sum_number)
print("the quotient of the number %0.4f" %quotient_number)

#mudulus = remainder
print(7%7)

# Even and odd number
for x in range (0,21):
    if (x%2==1):
        print(f"{x} is odd number")
    elif (x%2==0):
        print(f"{x} is even number")
