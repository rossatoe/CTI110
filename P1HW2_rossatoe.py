#This program will show you the expenses on your travel
#2/13/2023
# CTI-110 P1HW2 - Travel Expense
# Ezequiel Rossao
#
budget = float(input('Enter your Budget for this trip:\n'))
dest = input('Where are you traveling?\n')
gas = float(input('How much the gas cost?\n'))
accom = float(input('How much the accomodation cost?\n'))
food = float(input('How much the food cost?\n'))
expenses = gas + accom + food
result = budget - expenses
print ('You have', result, 'left on your budget after your trip to', dest, end='.')
