year = int(input('Escriba un año pasa saber si es bisiesto: '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Es bisiesto')
else:
    print('No es bisiesto')
           
