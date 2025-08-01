import random, sys
print('Rock, Paper, Scissors')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: #The main game loop
    print('%s Wins, %s Losses, %s Ties' %(wins, losses, ties))
    while True: # the player input() loop
        print('Enter you move: (r)ock (p)aper (s)cissors or (q)uit')
        player_move = input('>')
        if player_move == 'q':
            sys.exit() # quit the program

        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break #breakout player input loop
        print('Type one of r, s, p, or q.')

    # display what player chose:
    if player_move == 'r':
        print('Rock versus...')
    elif player_move == 'p':
        print('Paper versus...')
    elif player_move == 's':
        print('Scissors versus...')

    
    #display what computer chose:
    move_number = random.randint(1, 3)
    if move_number == 1:
        computer_move = 'r'
        print('Rock')
    
    elif move_number == 2:
        computer_move = 'p'
        print('Paper')
    
    elif move_number == 3:
        computer_move = 's'
        print('Scissors')

    # Display the record of win and loss and tie

    if player_move == computer_move:
        print("It's a tie")
        ties = ties + 1

    elif player_move == 'r' and computer_move == 's':
        print('You win')
        wins = wins +1

    elif player_move == 'p' and computer_move == 'r':
        print('You win')
        wins = wins + 1

    elif player_move == 's' and computer_move == 'p':
        print('You win')
        wins = wins + 1

    
    elif player_move == 'r' and computer_move == 'p':
        print('You lose')
        losses = losses + 1

    elif player_move == 'p' and computer_move == 's':
        print('You lose')
        losses = losses + 1

    elif player_move == 's' and computer_move == 'r':
        print('You lose')
        losses = losses + 1


