# CTI-110
# P4HW2 - Salary Calculator
# Ezequiel Rossato
# 4/19/2023
#
def mainLoop():
    name = ''
    employees = 0
    totalOverPay = 0
    totalRegPay = 0
    totalGrossPay = 0
    name = input("Enter employee's name or Done to terminate: ")
    while name != 'Done':
        #name = input("Enter employee's name or Done to terminate: ")
        employees += 1
        workHrs = int(input("How many hours did " + name + " work? "))
        payRate = float(input("What is " + name + "'s pay rate? "))
        overPay, regPay, overTime, grossPay = calculatePays(workHrs, payRate)
        printStatements(name, workHrs, payRate, overPay, regPay, overTime, grossPay)
        totalOverPay += overPay
        totalRegPay += regPay
        totalGrossPay += grossPay
        name = input("Enter employee's name or Done to terminate: ")
    totalPrint(employees, totalOverPay, totalRegPay, totalGrossPay)
    
def calculatePays(workHrs, payRate):
    if(workHrs > 40):
        overTime = workHrs - 40;
        overPay = (payRate * 1.5) * overTime ;
        regPay = payRate * 40
    else:
        overTime = 0
        overPay = 0
        regPay = payRate * workHrs
    grossPay = regPay + overPay

    return overPay, regPay, overTime, grossPay

def printStatements(name, workHrs, payRate, overPay, regPay, overTime, grossPay):
    print("Employee name: ", name)
    print()
    print(f'{"Hours Worked":<20}{"Pay Rate":<20}{"OverTime":<20}{"OverTime Pay":<20}{"RegHour Pay":<20}Gross Pay')
    print('----------------------------------------------------------------------------------------------------------------')
    print(f'{workHrs:.1f}{" ":<17}{payRate:.2f}{" ":<17}{overTime:.1f}{" ":<16}{overPay:.2f}{" ":<17}{regPay:.2f}{" ":<15}{grossPay:.2f}')

def totalPrint(employees, totalOverPay, totalRegPay, totalGrossPay):
    print(f'Total number of employees entered: {employees}')
    print(f'Total amount paid for overtime: ${totalOverPay:.2f}')
    print(f'Total amount paid for regular hours: ${totalRegPay:.2f}')
    print(f'Total amount paid in gross: ${totalGrossPay}')

mainLoop()

