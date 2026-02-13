# Nmae : Daniel nduati
# date : 13/02/2026
# formula to calculate AP

#calculating n term

a =int(input("Enter the first number : "))
n = int(input("Enter the number of terms : "))
d = int(input("Enter the common difference : "))

n_term = a+(n-1) *d
sn = (n/2) * (2*a+(n-1)*d)
print(f"the n term is : {n_term}")
print(f" sum of AP : {sn}")