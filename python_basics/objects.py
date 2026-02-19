#  Nmae : Daniel nduati
# date : 16/02/2026
# Classes(objects) in python

class Human:
    # 1.Find the attributes of human being
    type = "mammal"
    legs = 2
    brain = True
    warm_blooded = True
    city = "Nairobi"

    #2. wethen create a constructor for the class
    # The constructor will be used to create copies of the class
    def __init__(self, name, age,):
        self.human_name = name
        self.human_age = age

    def tell_story(self):
        print(f"Hello, my name is {self.human_name} and here is a story. Hammond you idiot.You bought the wrong car.")
# 3. create the humans
Clarkson = Human("Clarkson", 60)
Ashley = Human("Ashley", 20)

Clarkson.tell_story()

# Modify one object without affecting the other
print("Clarkson's city is ", Clarkson.city)
print("Ashley's city is ", Ashley.city)

Clarkson.city = "Jezza"

print("Clarkson's city is ", Clarkson.city)
print("Ashley's city is ", Ashley.city)