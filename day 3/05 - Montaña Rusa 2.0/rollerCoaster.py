height = int(input('Introduzca su altura en centimetros: '))
bill = 0

if height >= 120:
    print("Puede subir!")
    age = int(input('Introduzca su edad, porfavor: '))
    if age >= 18:
        price = '$12'
        print(f'El precio de la entrada es ${price}')
        bill = + 12
    elif age >= 12:
        price = '$7'
        print(f'El precio de la entrada es ${price}')
        bill = + 12

    else:
        price = '5'
        print(f'El precio de la entrada es ${price}')
        bill = + 12

else:
    print("No puede subir!")
