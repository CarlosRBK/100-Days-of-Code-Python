# import random

# print('''
#                            _._       _,._
#                         _.'   `. ' .'   _`.
#                 ,"""/`""-.-.,/. ` V'\-,`.,--/"""."-..
#               ,'    `...,' . ,\-----._|     `.   /   \
#              `.            .`  -'`"" .._   :> `-'   `.
#             ,'  ,-.  _,.-'| `..___ ,'   |'-..__   .._ L
#            .    \_ -'   `-'     ..      `.-' `.`-.'_ .|
#            |   ,',-,--..  ,--../  `.  .-.    , `-.  ``.
#            `.,' ,  |   |  `.  /'/,,.\/  |    \|   |
#                 `  `---'    `j   .   \  .     '   j
#               ,__`"        ,'|`'\_/`.'\'        |\-'-, _,.
#        .--...`-. `-`. /    '- ..      _,    /\ ,' .--"'  ,'".
#      _'-""-    --  _`'-.../ __ '.'`-^,_`-""""---....__  ' _,-`
#    _.----`  _..--.'        |  "`-..-" __|'"'         .""-. ""'--.._
#   /        '    /     ,  _.+-.'  ||._'   """". .          `     .__\
#  `---    /        /  / j'       _/|..`  -. `-`\ \   \  \   `.  \ `-..
# ," _.-' /    /` ./  /`_|_,-"   ','|       `. | -'`._,   L  \ .  `.   |
# `"' /  /  / ,__...-----| _.,  ,'            `|----.._`-.|' |. .` ..  .
#    /  '| /.,/   \--.._ `-,' ,          .  '`.'  __,., '  ''``._ \ \`,'
#   /_,'---  ,     \`._,-` \ //  / . \    `._,  -`,  / / _   |   `-L -
#    /       `.     ,  ..._ ' `_/ '| |\ `._'       '-.'   `.,'     |
#   '         /    /  ..   `.  `./ | ; `.'    ,"" ,.  `.    \      |
#    `.     ,'   ,'   | |\  |       "        |  ,'\ |   \    `    ,L
#    /|`.  /    '     | `-| '                  /`-' |    L    `._/  \
#   / | .`|    |  .   `._.'                   `.__,'   .  |     |  (`
#  '-""-'_|    `. `.__,._____     .    _,        ____ ,-  j     ".-'"'
#         \      `-.  \/.    `"--.._    _,.---'""\/  "_,.'     /-'
#          )        `-._ '-.        `--"      _.-'.-""        `.
#         ./            `,. `".._________...""_.-"`.          _j
#        /_\.__,"".   ,.'  "`-...________.---"     .".   ,.  / \
#               \_/"""-'                           `-'--(_,`"`-`
# ''')
# pokemons = ["Bulbasaur", "Charmander", "Squirtle", "Chikorita", "Cyndaquil"]
# print('Bienvenido a Pokethon')
# name = input('Como te llamas?: ' )
# print(f'Hola {name}')
# print('Bienvenido a Pokethon')
# optionOne = int(input('Te despiertas un Lunes, 18 de Septiembre del 2023, Es el gran dia!, Te daran tu primer pokemon!, responde con: "1" para quedarte a dormir, "2" para ir a la entrega de pokemones: ' ))
# if optionOne == 1:
#     print('Te quedas a dormir, game over')
# elif optionOne == 2:
#     print('Te iras a la entrega de pokemones!')
#     print('Haz llegado a la entrega de pokemones en Ciudad PALETA, que emocion!')
#     print('Oak: Hola a todos los futuros entrenadores pokemon!, soy el profesor Oak, estare llamando a los registrados para darles su primer pokemon!')
#     print('Blasto')
#     print('Elije una de las opciones!')
#     optionTwo = input('- Escribe "yo" para gritar presente, o guarda silencio escribiendo "silencio": ').lower()
#     if optionTwo == 'yo':
#         print('Te gritas presente!')
#         print('No eres Blasto, has perdido el juego!')
#     elif optionTwo == 'silencio':
#         print('Guardas silencio...')
#         print('...')
#         print('..')
#         print('Blasto sube y coge la pokebola...')
#         pokemonBlasto = random.choice(pokemons)
#         pokemons.remove(pokemonBlasto)
#         print(f'Blasto ha obtenido a {pokemonBlasto}')
#         print(f'Oak: Felicidades Blasto, {pokemonBlasto} es un muy buen pokemon, espero que sean buenos amigos... ')
#         print(f'Blasto: Gracias pokemon estoy muy contento con {pokemonBlasto}!')
#         print('Blasto baja muy contento, y el profesor Oak llama al siguiente futuro entrenador...')
#         print(f'Los pokemons restantes son: {pokemons}')
#         print(f'Oak: {name}!')
#         optionThree = input('- Escribe "yo" para gritar presente, o guarda silencio escribiendo "silencio": ').lower()
#         if optionThree == 'silencio':
#             print('Guardas silencio...')
#             print('...')
#             print('..')
#             print('No has subido y has perdido el juego!')
#         elif optionThree == 'yo':
#             print(f'{name}: Presente!')
#             print(f'{name} sube a las escaleras..')
#             print(f'Oak: Hola {name}, elije una pokebola, buena suerte!')
#             eleccionPokebola = input('- Hay 3 pokebolas en la superficie elije uno de los 3!, escribe "Escoger" para agarrar un pokemon, o escribe "Irse" para irse corriendo!: ').lower()
#             if eleccionPokebola == 'escoger':
#                 pokemonJugador = random.choice(pokemons)
#                 pokemons.remove(pokemonJugador)
#                 print(f'Obtuviste a {pokemonJugador}')
#                 print(f'Oak: Felicidades {name}, {pokemonJugador} es una muy buena opcion espero que sean grandes amigos!')
#             elif eleccionPokebola == 'irse':
#                 print(f'{name}: Me voy!')   
#                 print(f'{name} perdio la oportunidad y no se podra convertir en un entrenador pokemon!, GAME OVER')   
#     else: 
#         print('Elije una opcion valida!')	
# else:
#     print('Ingresa un numero valido!')
