#  Nmae : Daniel nduati
# Date : 23/02/2026
# progrma to show class in python
class Car():
    #attribute of the car
    def __init__(self, make, model, color, year):
        self.make
        self.model
        self.color
        self.year 
# print car details
    def print_details(self, make, model, color, year):
        print(f"Car details: {make} {model} of color {color} was made in the year {year}")
    
    make = "Mercedes"
    model = "AMG GT Black Series"
    color = "Black"
    year = "2017"

# instantiate a class subject
my_car = Car("Mercedes", "AMG GT Black Series", "Black", "2017")
another_car = Car("Range Rover", "Velar", "Silver", "2020")

my_car.print_details("Mercedes", "AMG GT Black Series", "Black", "2017")

