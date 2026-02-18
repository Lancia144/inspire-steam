# Nmae : Daniel nduati
# date : 18
# 18/02/2026
# Program to show list in python
# List of friends

friends =["Leclerc","Alonso","Michael","Senna"]
friends.sort()
print(friends)

friends.reverse()
print(friends)

friends.append("Verstappen")
print(friends)

new_friends = ["Riccardo","Yuki","Lauda","Kimi"]
print(len(new_friends))

# New list of students
students = friends + new_friends
print(students)

students.pop()
print(students)
students.insert(4,"Vettel")
print(students)

students.insert(9,"Nico")
print(students)

students.extend("Carlos")
print(students)

students.remove("Nico")
print(students)

new_students = students.copy()
print(students)