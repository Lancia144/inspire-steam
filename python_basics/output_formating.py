# Nmae : Daniel nduati
# date : 17/02/2026
# program to format output in different styles

name = "Daniel Nduati" # name
weight = 76 # weight in kg
fav_team = "Arsenal"
height = 176 # height in kgs

# 1.format using print(f"{}")
print(f"My names is {name} and I weigh {weight} kgs.")

# Using f string
msg = f"my name is {name} and I support {fav_team}"
print(msg)

# 3.Using curly bracket and .format
print("my name {0} and I am {1} cm tall" .format (name,height))

# 4.Using output specifies %s
import math
print('The value of pi is approximately %5.3f.' % math.pi)
print("My support %s" %fav_team)
