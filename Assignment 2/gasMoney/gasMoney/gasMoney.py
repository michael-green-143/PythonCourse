# This program asks the user for the gas mileage (MPG) on their vehicle, 
# along with how far they plan on traveling in miles. 
# The program will then calculate the gas expenses based on their entry and 
# a gas price of $2.21 per gallon, and displays the expenses.
#
# Created by Michael Green - 1/27/21

GAS = 2.21 # set gas price

milesPerGallon = int(input("Please enter the gas mileage or the approximate miles per gallon your vehicle gets: "))
milesTraveled = int(input("Please enter (in miles) how far you plan on traveling: "))

gasExpenses = float((milesTraveled / milesPerGallon) * GAS)

print("The total expenses for this trip will be $", gasExpenses)