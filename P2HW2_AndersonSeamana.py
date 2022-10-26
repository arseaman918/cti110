# CTI-110
# P2HW2 - List
# Your Name 
# Date
#
mod1Grade = float(input('Enter grade for Module 1: '))
mod2Grade = float(input('Enter grade for Module 2: '))
mod3Grade = float(input('Enter grade for Module 3: '))
mod4Grade = float(input('Enter grade for Module 4: '))
mod5Grade = float(input('Enter grade for Module 5: '))
mod6Grade = float(input('Enter grade for Module 6: '))



print()
print('------------Results------------')

modgrades = {mod1Grade, mod2Grade, mod3Grade, mod4Grade, mod5Grade, mod6Grade}
avg_grades = sum(modgrades) / 6
print('Lowest Grade:',' ', min(modgrades))
print('Highest Grade:','', max(modgrades))
print('Sum of Grades:','', sum(modgrades))
print(f'Average         {avg_grades:.2f}')
print('----------------------------------------')
