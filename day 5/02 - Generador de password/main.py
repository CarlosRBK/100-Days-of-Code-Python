import random
#Password Generator Project
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

passwordOrdenado = []
passwordHard = []
resultado = ''

for index, letter in enumerate(letters):
    if index < nr_letters:
        random_letters = random.randint(0, (len(letters) - 1))
        passwordOrdenado.append(letters[random_letters])

for index, number in enumerate(numbers):
    if index < nr_numbers:
        random_numbers = random.randint(0, (len(numbers) - 1))
        passwordOrdenado.append(numbers[random_numbers])

for index, symbol in enumerate(symbols):
    if index < nr_symbols:
        random_symbols = random.randint(0, (len(symbols) - 1))
        passwordOrdenado.append(symbols[random_symbols])

for index, caraceter in enumerate(passwordOrdenado):
    if index < len(passwordOrdenado):
        random_caracter = random.randint(0, (len(passwordOrdenado) - 1))
        passwordHard.append(str(passwordOrdenado[random_caracter]))

for index, letra in enumerate(passwordHard):
    if index < len(passwordHard):
        resultado += letra


print(resultado)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
