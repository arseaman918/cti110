# CTI-110
# P3HW2 - Salary
# Anderson Seaman   
# 10/30/22
#

employee = input('Enter employees name: ')
hours = float(input('Enter number of hours worked: '))
rate = float(input('Enter employees pay rate: '))
if hours > 40:
    normal_pay = (40 * rate)
overtime = hours % 40
overtime_pay = overtime * (rate * 1.5)

print('---------------------------------------')
print('Employees name: ', employee)
print()
print('Hours Worked     Pay Rate     Overtime     OverTime Pay     RegHour Pay     Gross Pay')
print('-----------------------------------------------------------------------------------------------------------------------------------------')
print(f'{hours}                    {rate}              {overtime}            {overtime_pay}                  ${normal_pay}                ${normal_pay + overtime_pay}')




