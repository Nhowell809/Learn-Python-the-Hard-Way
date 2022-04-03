#variable for types of people set to 10.
types_of_people = 10
# variable x assigned to format There are insert variable types_of_people types of people.
x = f"There are {types_of_people} types of people."

#varirable binary set to binary
binary = "binary"
#variable do not set to don't
do_not = "don't"
#variable y set to forma those who know insert variable binary and those who insert variable do_not
y = f"Those who know {binary} and those who {do_not}."

#print variable x
print(x)
#print variable y
print(y)

#print format I said: insert variable x.
print(f"I said: {x}")
#print format I also said: insert variable y.
print(f"I also said: '{y}'")

#set variable hilarious to false
hilarious = False
#set variable joke_evaluation to isn't that joke so funny?
joke_evaluation = "Isn't that joke so funny?! {}"

#print variable joke_evaluation format insert variable hilarious
print(joke_evaluation.format(hilarious))

#set variable w to this is the left side of...
w = "This is the left side of..."
#set variable e to a string with a right side.
e = "a string with a right side."

#print variable e concatenated with e. 
print(w + e)
