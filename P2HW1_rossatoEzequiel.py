# This program Shows all the expensives of your travel
# 2/27/2023
# CTI-110 P2HW1 - Travel
# Ezequiel Rossato
#
# Display "Enter budget:"
# Input budget
# Display "Where are you traveling?"
# Input dest
# Display "How much the gas cost?"
# Input gas
# Display "How much the accomodation cost?"
# Input accom
# Display "How much the food cost?"
# Input food
# Calculate the expenses
# Calculate the remaining balance
# Display "------------Travel Expenses------------"
# Display "Location:", dest
# Display "Initial Budget: ", budget
# Display "Fuel: ", gas
# Display "Accomodation:", accom
# Display "Food:, food
# Display "---------------------------------------"
# Display "Remaining Balance:", result
#
budget = float(input('Enter budget:\n'))
dest = input('Where are you traveling?\n')
gas = float(input('How much the gas cost?\n'))
accom = float(input('How much the accomodation cost?\n'))
food = float(input('How much the food cost?\n'))
expenses = gas + accom + food
result = budget - expenses
print('------------Travel Expenses------------')
print('Location:', dest)
print('Initial Budget: ', budget)
print('Fuel:', gas)
print('Accomodation:', accom)
print('Food:', food)
print('---------------------------------------')
print ('Remaining Balance:', result)
