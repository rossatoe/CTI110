# CTI-110
# P2HW2 - List
# Ezequiel Rossato
# 2/27/2023
#
# Display "Enter your grade in module 1: "
# Input mod1
# Display "Enter your grade in module 2: "
# Input mod2
# Display "Enter your grade in module 3: "
# Input mod3
# Display "Enter your grade in module 4: "
# Input mod4
# Display "Enter your grade in module 5: "
# Input mod5
# Display "Enter your grade in module 6: "
# Input mod6
# Create a list and input the module values
# Display "------------Results------------"
# Display "Your lower grade is:"
# Display "Your highest grade is:"
# Display "All your grades sum are:"
# Calculate average
# Display "Your grade's average is:"
# Display "-------------------------------"
mod1 = float (input('Enter your grade in module 1: '))
mod2 = float (input('Enter your grade in module 2: '))
mod3 = float (input('Enter your grade in module 3: '))
mod4 = float (input('Enter your grade in module 4: '))
mod5 = float (input('Enter your grade in module 5: '))
mod6 = float (input('Enter your grade in module 6: '))
gradeList = [mod1, mod2, mod3, mod4, mod5, mod6]
print('------------Results------------')
print('Your lower grade is:', min(gradeList))
print('Your highest grade is:', max(gradeList))
print('All your grades sum are:', sum(gradeList))
gradesAvrg = sum(gradeList) / len(gradeList)
print("Your grade's average is:", gradesAvrg)
print('-------------------------------')
