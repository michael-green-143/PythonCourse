# This program asks the user for the temperature in fahrenheit and 
# returns the temperature in celsius.
# 
# Created by Michael Green - 1/25/21

fTemp = float(input("Please enter the temperature in fahrenheit: ")) # fahrenheit
cTemp = float(((fTemp - 32) * (5 / 9))) # celsius

print(fTemp, "degrees in fahrenheit is equal to", cTemp, "degrees in celsius.")

