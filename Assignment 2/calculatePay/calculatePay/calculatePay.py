# This program calculates the take home pay for the user based on their hours and gross pay,
# along with the appropriate taxes that need to be figured in. 
#
# Created by Michael Green, 1/25/21

OVERTIME = 40 # Max amount of hours before overtime pay (1.5 times) kicks in

# This next constant holds the total amount of taxes taken out of gross pay 
TAXES = 0.374 # FICA = 6.2%, Medicare = 1.45%, State Tax = 4.25%, Federal Tax = 24%, City Tax = 0.9%, Park Tax = 0.6%

fName = input("Hello! Please enter your first name: ")
hoursWorked = float(input("Please enter the amount of hours you worked this week: "))
hourlyRate = float(input("Please enter how much you make each hour: "))

grossPay = 0 # We will assign the total gross pay (before taxes) to this variable

overtimeHours = hoursWorked - OVERTIME # This variable will hold the amount of overtime hours

# This will check if we even have overtime hours 
if overtimeHours < 0:
    overtimeHours = 0

# This next line calculates and holds the total gross pay of the user
grossPay = round((1.5 * hourlyRate * overtimeHours) + (hourlyRate * (hoursWorked - overtimeHours)), 2)

# This line calculates and holds the total take home pay for the week (net? pay)
homePay = round(grossPay - (grossPay * TAXES), 2)

print("So", fName, ",")
print("Hours worked:", hoursWorked)
print("Overtime hours:", overtimeHours)
print("Hourly pay:", hourlyRate)
print("Gross pay:", grossPay)
print("Amount taken out of pay for taxes:", round((grossPay * TAXES), 2))
print("Take home pay:", homePay)