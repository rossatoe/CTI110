#This program will show you the expenses on your travel
#2/13/2023
# CTI-110 P1HW2 - Travel Expense
# Ezequiel Rossao
#
# Display "Enter your Budget for this trip:"
# Input budget
# Display "Where are you traveling?"
# Input dest
# Display "How much the gas cost?"
# Input gas
# Display "How much the accomodation cost?"
# Input accom
# Display "How much the food cost?"
# Input food
# sum the expenses
# substract the expenses from the budget
# Display "You have", result, "left on your budget after your trip to", dest
#
budget = float(input('Enter your Budget for this trip:\n'))
dest = input('Where are you traveling?\n')
gas = float(input('How much the gas cost?\n'))
accom = float(input('How much the accomodation cost?\n'))
food = float(input('How much the food cost?\n'))
expenses = gas + accom + food
result = budget - expenses
print ('You have', result, 'left on your budget after your trip to', dest, end='.')
