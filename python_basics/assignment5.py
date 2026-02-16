# Nmae : Daniel nduati
# date : 16/02/2026

salary = int(input("Enter your gross salary"))
if  salary <= 50000:
    tax = (2.5 * salary) /100
    net_salary = salary - tax
    print(f"Gross salary = {salary}")
    print(f"Net salary = {net_salary}")
    print(f"Tax = {tax}")

elif salary >50000 <100000:
    tax = (4.5 * salary) /100
    net_salary = salary - tax
    print(f"Gross salary = {salary}")
    print(f"Net salary = {net_salary}")
    print(f"Tax = {tax}")
    
elif salary >100000:
    tax = (4.5 * salary) /100
    net_salary = salary - tax
    print(f"Gross salary = {salary}")
    print(f"Net salary = {net_salary}")
    print(f"Tax = {tax}")
