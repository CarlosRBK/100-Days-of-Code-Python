import random

names_string = input("Give me everybody's name, separated by a comma: ")
names = names_string.split(", ")
random_integer = random.randint(0, len(names)-1)
ganador = names[random_integer]

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(arr[-1])