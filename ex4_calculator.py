print("Enter the number of cars in todays fleet:", end=' ')
cars =int(input())
space_in_a_car = 4
print("Enter the number of drivers working today:", end=' ')
drivers = int(input())
print("Enter the total number of todays passengers:", end= ' ')
passengers = int(input())
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity =cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print(f"There are {cars} cars availabe.")
print(f"There are only {drivers} drivers available.")
print(f"There will be {cars_not_driven} empty cars today.")
print(f"We can transport {carpool_capacity} people today.")
print(f"We have {passengers} to carpool today.")
print(f"We need to put about {average_passengers_per_car} in each car.")
