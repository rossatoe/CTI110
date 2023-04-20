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
    else:
        overTime = 0
        overPay = 0
    regPay = payRate * 40
    grossPay = regPay + overPay

    return overPay, regPay, overTime, grossPay

def printStatements(name, workHrs, payRate, overPay, regPay, overTime, grossPay):
    print("Employee name: ", name)
    print()
    print(f'{"Hours Worked":<20}{"Pay Rate":<20}{"OverTime":<20}{"OverTime Pay":<20}{"RegHour Pay":<20}{"Gross Pay":<20}')
    print('-------------------------------------------------------------------------------------------------------------')
    print(f'{workHrs:<20}{payRate:<20}{overTime:<20}{overPay:<20}{regPay:<20}{grossPay:<20}')

def totalPrint(employees, totalOverPay, totalRegPay, totalGrossPay):
    print(f'Total number of employees entered: {employees}')
    print(f'Total amount paid for overtime: ${totalOverPay:.2f}')
    print(f'Total amount paid for regular hours: ${totalRegPay:.2f}')
    print(f'Total amount paid in gross: ${totalGrossPay}')

mainLoop()

