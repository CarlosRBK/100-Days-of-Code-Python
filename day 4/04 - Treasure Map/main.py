row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]

map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
an_int  = input('Donde crees que se encuentra el tesoro?: ')
list_of_digits = []
for x in str(an_int):
    list_of_digits.append(int(x))

num_uno = list_of_digits[1]-1
num_dos = list_of_digits[0]-1

map[num_uno][num_dos] = 'X'
print(f"{row1}\n{row2}\n{row3}")
