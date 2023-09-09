f = str(input())
s = str(input())

if (f == ('scissors') and s == ('paper')) or (f == ('paper') and s == ('rock')):
    print('player1 wins')
elif (f == ('rock') and s == ('lizard')) or (f == ('lizard') and s == ('Spock')):
    print('player1 wins')
elif (f == ('Spock') and s == ('scissors')) or (f == ('scissors') and s == ('lizard')):
    print('player1 wins')
elif (f == ('lizard') and s == ('paper')) or (f == ('paper') and s == ('Spock')):
    print('player1 wins')
elif (f == ('Spock') and s == ('rock')) or (f == ('rock') and s == ('scissors')):
    print('player1 wins')
elif (f == ('rock') and s == ('rock')) or (f == ('paper') and s == ('paper')) or (f == ('scissors') and s == ('scissors')):
    print('draw')
elif (f == ('lizard') and s == ('lizard')) or (f == ('Spock') and s == ('Spock')):
    print('draw')
else:
    print('player2 wins')

