# This program (gradeCalc) takes input of grades from the user or instructor,
# and provides the average scores and letter grades of an assignment from a group of students. 
# The program displays this and how many student grades were entered.
#
# Created by Michael Green, 2/3/21

grades = [] # this list will hold all grades entered
# These variables will hold the amount of letter grades for each letter (A,B,C,D,F)
aGrades = 0
bGrades = 0
cGrades = 0
dGrades = 0
fGrades = 0

# first entry of grade
entry = int(input("Please enter the grade between 0 and 100, or '-1' if there is no grade to enter: "))

# this will continue the grade entering; if the user enters -1, the loop ends and indicates that there is no more grades to enter
while entry != -1: 
    grades.append(entry) # the append command will add the users entry to our "grades" list
    entry = int(input("Please enter the grade between 0 and 100, or '-1' if there is no grade to enter: "))

# need to find length of list "grades"
length = len(grades)

total = 0 # will be total amount and will be divided by number of students

# This loop is to find the total score of all students and amount of letter grades (A,B,C,D, or F) received
for num in grades:
    total += num
    if num <= 100 and num >= 90:
        aGrades += 1
    if num <= 89 and num >= 80:
        bGrades += 1
    if num <= 79 and num >= 70:
        cGrades += 1
    if num <= 69 and num >= 60:
        dGrades += 1
    if num < 60:
        fGrades += 1

# this will compute the average grade of all students
average = total / len(grades)

# display information
print("The average score for all the students is", average)
print("There were", length, "grades entered.")
print("A grades:", aGrades)
print("B grades:", bGrades)
print("C grades:", cGrades)
print("D grades:", dGrades)
print("F grades:", fGrades)