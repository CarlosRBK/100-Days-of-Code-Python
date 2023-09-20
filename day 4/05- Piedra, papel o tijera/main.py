import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

opciones = []
opciones.append(rock)
opciones.append(paper)
opciones.append(scissors)
random_integer = random.randint(0, (len(opciones) - 1))
print(f'{opciones[0]}\n{opciones[1]}\n{opciones[2]}')

botOp = int(random_integer)
bot = opciones[botOp]
playOp = int(
    input('What choose? Type 0 for Rock, 1 for Paper or 2 for Scissor: '))
player = opciones[playOp]

if playOp == 0 and botOp == 2 or playOp == 1 and botOp == 0 or playOp == 2 and botOp == 1:
  print(f'{player}\nComputer chose:\n{bot}\nYou win!')
elif playOp == botOp:
  print(f'{paper}\nComputer chose:\n{bot}\nEmpate!')
else:
  print(f'{paper}\nComputer chose:\n{bot}\nPerdiste!')
