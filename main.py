from C4 import C4

def get_symbol(player):
  yn = input(f'\nPlease choose a token to use for \'{player}\' (It can be any character except for zero. Make sure your token is just one character) :')
  while True:
    if yn != '0' and len(yn) == 1:
      return yn
    
    yn = input(f'\n Symbol is not permissable, please choose another token for \'{player}\' (Make sure your token is not \'0\' and it is just one character like \'@\', \'#\', \'A\', or \'4\'.) : ')

def get_yn():
  while True:
    
    yn = input('\n Enter a y for yes or a n for no(in lowercase please):')
    if yn == 'y':
      return True
    
    elif yn == 'n':
      return False

def get_move(player):
  move = input(f'\n \'{player}\', enter a number from 1 to 7:')
  while True:
    
    if move  in [f'{i}' for i in range(1, 8)]:
      return move
    
    move = input(f' Input is invalid, \'{player}\' make sure your input is a number from 1 to 7: ')

player1 = input('\nPlease choos a name for player 1: ')
player2 = input('\nPlease choos a name for player 2: ')
symbol1 = get_symbol(player1)
symbol2 = get_symbol(player2)
game = C4(player1, player2, symbol1, symbol2)
player = [player1, player2]
while game.game_finished == 0:
  player_move = get_move(player[1 - game.turn % 2])
  game.one_turn(player_move)
  if game.game_finished == 1:
    print('Would you like to continue the game?')
    yn = get_yn()
    if yn == True:
      game.reset()
      
    else:
      print('\nThank you for playing!!!')