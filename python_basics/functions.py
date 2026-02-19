# Nmae : Daniel nduati
# date : 16/02/2026
# program to show how to define and call a function

def cook_eggs():
    oil = "20ml"
    pan = True
    fire = True
    eggs = 2
    
    print(f"The pan is {pan}, oil is {oil}, fire is {fire}, and cookeggs are {eggs} eggs")

print("Here is statement 1")
print("Here is statement 2")

cook_eggs()

print("Here is statement 3")

# bus fare creating function
def create_fare(route, distance, is_rush_hour):
    fare = distance * 10
    if is_rush_hour == True:
        fare =fare * 1.5
    print(f"The fare on route {route} is {fare} ")

    return fare

returned_fare = create_fare("Juja-Allsops", 7,is_rush_hour = True)
print(f"Fare returned is {returned_fare}")

# passing a list as parametrer
def write_all_interests(interests):
    for interest in interests:
        print(f"I am interested in {interest}")

interests = ["Arsetto corsa", "F1 ", "painting", "cooking", "gaming"]

write_all_interests(interests)