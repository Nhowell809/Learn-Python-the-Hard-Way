#how many cars we have
cars = 100

#How many people fit in a car
space_in_a_car = 4.0

#How many drivers we have
drivers = 30

#How many passengers we need to service
passengers = 90

#calculation for cars not being driven
cars_not_driven = cars - drivers

#calculation for cars that can be driven equal to the number of drivers
cars_driven = drivers

#calculation for carpool capacity based on cars that can be driven multiplied by the space in a car
carpool_capacity = cars_driven * space_in_a_car

#calculation for average passengers per car based on total passengers divded by cars that can be driven
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars availabe.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
