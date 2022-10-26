# Budget break down of a trip
# 09/21/22
# CTI-110 P1HW2 - Travel Expense
# Anderson Seaman
#
print('Enter Budget: ', end=' ')
budget = float(input())
print('Enter your travel destination: ', end=' ')
destination = input()
print('How much do you think you will spend on gas? ', end =' ')
num1 = float(input())
print('Approximately, how much will you need for accomadation/hotels?: ', end =' ')
num2 = float(input())
print('Last, how much do you need for food?', end =' ')
num3 = float(input())
print('------------Travel Expenses-----------')
print('Location: ', destination)
print('Initial Budget: ', budget)
print()
print('Fuel: ', num1)
print('Accomodations: ', num2)
print('Food: ', num3)
print()
print('Remaining balance: ', budget-num1-num2-num3)

# The numbers being shown and the total cost of all three variables being subracted from our initial budget
