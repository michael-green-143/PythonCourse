# This program loops through a list from 147 to 62, subtracting 3 during each iteration.
# The program then prints the amount of times it looped, along with the ending number.
#
# Created by Michael Green, 2/1/21

i = 147
loopAmount = 0

while i >= 62:
    print(i)
    i -= 3
    loopAmount += 1

print("Ending number:", i)
print("Looped", loopAmount, "times")