# Nmae : Daniel nduati
# Date : 24/02/2026
# Program to perform file operations

# Create new file
new_file = open("student_data.txt", "r+")
#write new file
new_file.write("{Student Name: Alonso  ,ID:78654398, Email: alonso@gmail.com}")

#read new file
data = new_file.read()
print(data)
new_file.close()
#delete file
import os
os.remove("remove.txt")
# delete folder
os.rmdir("remove_dir")