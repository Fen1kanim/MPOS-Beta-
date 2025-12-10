from subprocess import call

stdin = input('''
1. 2.5D labyrinth
2. guess a random number
3. pong

choose a game(123): ''')

[call(["python", "./keywords/games/labyrinth.py"]) if stdin == "1" else None]
[call(["python", "./keywords/games/guess.py"]) if stdin == '2' else None]
[call(["python", "./keywords/games/pong.py"]) if stdin == '3' else None]
if stdin != '1' or stdin != '2' or stdin != '3':
    print('''
try again''')
