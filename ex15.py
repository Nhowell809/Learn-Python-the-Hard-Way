# from system import argument variable feature
from sys import argv

# variables for argv are script and filename.
script, filename = argv

# varibale text will open the afformentioned filename.
txt = open(filename)

# print out here is your file, with the variable file name present.
print(f"Here's your file {filename}:")
# print out variable txt (file we loaded into the program) to be read by python.
print(txt.read())

# print Type the filename again
print("Type the filename again:")
# file again is a variable where user inputs the name of the file to open
file_again = input("> ")

#variable text again opens the previous lines entered file.
txt_again = open(file_again)

# prints the text from the above variable. 
print(txt_again.read())
