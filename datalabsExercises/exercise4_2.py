# Write a program to prompt the user for hours and hourly pay so that
# calculate the total pay. Payment should be the normal rate for hours up to 40 and
# 1.5 for the hourly rate for all hours worked over 40. Put the logic to make the
# calculate the pay in a function called computepay() and use it
# function to do the calculation. The function must return a value. Use 45
# hours and a rate of 10.50 per hour to try the program (fee must if 498.75).
# you need to use input to read a string and float() to convert
# the string to a number. Don't worry about the error checking user input.

hours = float(input("Enter your total working hours per week :"))
wagePerHour = float(input("Enter wage per hour :"))

def computepay(time,wage):
    if hours <= 40:
        total = wagePerHour * hours
        return total
    elif hours > 40:
        total = 40 * 120 + (hours - 40) * 1.5 * 10.50
        return total

print(computepay(hours,wagePerHour))