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
# Display "------------Travel Expenses------------"
# Display "Location:, dest
# Display "Initial Budget", budget
# Display "Fuel:", gas
# Display "Accomodation", accom
# Display "Food:", food
# Display "Remaining Balance:", result
#
budget = float(input('Enter your Budget for this trip:\n'))
dest = input('Where are you traveling?\n')
gas = float(input('How much the gas cost?\n'))
accom = float(input('How much the accomodation cost?\n'))
food = float(input('How much the food cost?\n'))
expenses = gas + accom + food
result = budget - expenses
print ('------------Travel Expenses------------')
print ('Location:', dest)
print ('Initial Budget', budget)
print ('Fuel:', gas)
print ('Accomodation', accom)
print ('Food:', food)
print ('Remaining Balance:', result)
