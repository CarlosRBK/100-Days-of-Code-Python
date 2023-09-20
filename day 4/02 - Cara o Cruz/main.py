import random

options = ['CARA', 'CRUZ']

random_integer = random.randint(0, 1)
ganador = options[random_integer]

eleccion = str(input('"CARA" O "CRUZ"?: ')).upper()
if eleccion == ganador:
    print('Ganaste!')
else:
    print('Perdiste!')
