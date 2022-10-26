mileage = float(input())
price_per_gallon = float(input())

 

miles_20 = (20 / mileage) * price_per_gallon
miles_75 = (75 / mileage) * price_per_gallon
miles_500 = (500 / mileage) * price_per_gallon

print(f'{miles_20:.2f} {miles_75:.2f} {miles_500:.2f}')
