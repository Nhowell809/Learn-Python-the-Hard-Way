# define the variable cheese and crackers to take two things.
# print varius statements using the two things in () etc
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# print that this section will use numbers given directly. The 20 refers to cheese_count and 30 refeers to boxes of crackers.
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# 10 refers to cheese count, 50 to boxes of crackers
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
# temporary variable to be used in the def cheese and crackers.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
