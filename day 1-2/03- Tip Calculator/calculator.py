total = float(input('What whas the total bill?'))
porcent = (int(input('What porcentage tip would you like to give? 10, 12, or 15?')) + 100) / 100
peopleQuantity = int(input('How many people to split the bill?'))
result = total * porcent / peopleQuantity
print(f'Each person should pay ${result:.2f}')