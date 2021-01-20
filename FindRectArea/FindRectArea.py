# This program asks the user for the length and width of a rectangle,
# and their first and last name. The program prints out the area,
# along with the user's name.
#
# Michael Green - 1/19/21

l = int(input("Please enter the length of a rectangle: "))
w = int(input("and now the width: "))

first = input("Please enter your first name: ")
last = input("and now your last name: ")

print("Hey", first, ", the length and width you entered were", l, "and", w, ".")
print("Mr", last, ", the area is", l * w)