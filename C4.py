class C4:
  def __init__(self, player1, player2):
    self.player1 = player1
    self.player2 = player2
    self.grid = [[0 for i in range(7)] for i in range(6)]
    self.initial_screen()
    
    
  def initial_screen(self):
    print('-'*30)
    print('Welcome to Connect Four.')
    print('-'*30)
    print('Connect four is two player game where each player chooses a token and then take turns entering thier respective token into a grid where the piece falls to the lowest available space within the column chosen. The goal of the game is to form a horizontal, vertical, or diagonal line of four of one\'s own token.')
    print('Let us start. The following is the empty gird.')
    self.print_grid()
    
  def print_grid(self):
    grid = self.grid
    print('+-'*7 + '+')
    print('|{}|{}|{}|{}|{}|{}|{}|'.format(grid[0][0], grid[0][1], grid[0][2], grid[0][3], grid[0][4], grid[0][5], grid[0][6], ))
    print('+-'*7 + '+')
    print('|{}|{}|{}|{}|{}|{}|{}|'.format(grid[1][0], grid[1][1], grid[1][2], grid[1][3], grid[1][4], grid[1][5], grid[1][6], ))
    print('+-'*7 + '+')
    print('|{}|{}|{}|{}|{}|{}|{}|'.format(grid[2][0], grid[2][1], grid[2][2], grid[2][3], grid[2][4], grid[2][5], grid[2][6], ))
    print('+-'*7 + '+')
    print('|{}|{}|{}|{}|{}|{}|{}|'.format(grid[3][0], grid[3][1], grid[3][2], grid[3][3], grid[3][4], grid[3][5], grid[3][6], ))
    print('+-'*7 + '+')
    print('|{}|{}|{}|{}|{}|{}|{}|'.format(grid[4][0], grid[4][1], grid[4][2], grid[4][3], grid[4][4], grid[4][5], grid[4][6], ))
    print('+-'*7 + '+')
    print('|{}|{}|{}|{}|{}|{}|{}|'.format(grid[5][0], grid[5][1], grid[5][2], grid[5][3], grid[5][4], grid[5][5], grid[5][6], ))
    print('+-'*7 + '+')