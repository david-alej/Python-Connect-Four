class C4:
  def __init__(self, player1, player2, player1_symbol, player2_symbol):
    self.player1 = player1
    self.player2 = player2
    self.symbol1 = player1_symbol
    self.symbol2 = player2_symbol
    self.grid = [[0 for i in range(7)] for i in range(6)]
    self.turn = 0
    self.game_finished = 0
    self.initial_screen()
    self.turn += 1
    
  def initial_screen(self):
    print('-'*30)
    print('Welcome to Connect Four.')
    print('-'*30)
    print('Connect four is two player game where each player chooses a token and then take turns entering thier respective token into a grid where the piece falls to the lowest available space within the column chosen. The goal of the game is to form a horizontal, vertical, or diagonal line of four of one\'s own token.')
    print('Let us start. The following is the empty gird. Where each player will pick a column number, shown on the top of the grid.')
    self.print_grid()
    
  def print_grid(self):
    grid = self.grid
    print(f'\n The grid for turn {self.turn} is shown below.\n')
    print(' 1 2 3 4 5 6 7 ')
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
    print('+-'*7 + '+\n')
    
  def one_turn(self, player_move):
    column = int(player_move) - 1
    symbol = [self.symbol1, self.symbol2]
    if self.game_finished == 0:
      for row in [5 - i for i in range(6)]:
        if self.grid[row][column] == 0:
          self.grid[row][column] = symbol[1 - self.turn % 2]
          self.print_grid()
          
          self.game_status()
          if self.game_finished == 1:
            player = [self.player1, self.player2]
            print(f'Congragulations \'{player[1 - self.turn % 2]}\', has won the game!!!!!!! Check the previous grid to see where \'{player[1 - self.turn % 2]}\' got the connect four.')
            
          self.turn += 1
          return
      
      return None  
    else:
      print('The game is finsihed.')
    
  def game_status(self):
    if self.turn < 6:
      return 
    
    grid = self.grid
    row_count = 1
    for j in range(6):
      for i in range(1,7):
        if grid[j][i] == grid[j][i - 1] and grid[j][i] != 0:
          row_count += 1
          if row_count == 4:
            self.game_finished = 1
            return 1
            
        else:
          row_count = 1
            
    column_count = 1
    for j in range(7):
      for i in range(1,6):
        if grid[i][j] == grid[i - 1][j] and grid[i][j]:
          column_count += 1
          if column_count == 4:
            self.game_finished = 1
            return 1
            
        else:
          column_count = 1
    
    for i in range(3, 6):
      self.check_forward_slash(i + 1, i, 0)
      if i == 5:
        for j in range(1, 4):
          self.check_forward_slash(i + 2 - j, i, j)
    
    if self.game_finished == 1:
      return 1
          
    for i in range(3, 6):
      self.check_backward_slash(i + 1, i, 6)
      if i == 5:
        for j in range(1, 4):
          self.check_backward_slash(i +2 - j, i, 6 - j)
    
    if self.game_finished == 1:
      return 1
      
    return 0
    
  # Helper funciton
  def check_forward_slash(self, line_length, start_row, start_column):
    foward_slash_count = 1
    for i in range(1, line_length):
      if self.grid[start_row - i][i + start_column] == self.grid[start_row - i + 1][i - 1 + start_column] and self.grid[start_row - i][i + start_column] != 0:
        foward_slash_count += 1
        if foward_slash_count == 4:
          self.game_finished = 1
          return
        
      else:
        foward_slash_count = 1
          
  # Helper funciton
  def check_backward_slash(self, line_length, start_row, start_column):
    foward_slash_count = 1
    for i in range(1, line_length):
      if self.grid[start_row - i][start_column - i] == self.grid[start_row - i + 1][start_column - i + 1] and self.grid[start_row - i][start_column - i] != 0:
        foward_slash_count += 1
        if foward_slash_count == 4:
          self.game_finished = 1
          return
        
      else:
        foward_slash_count = 1
        
  def reset(self):
    self.turn = 0
    self.game_finished = 0
    self.grid = [[0 for i in range(7)] for i in range(6)]
    print('\n\n')
    self.print_grid()
    print(f'\nNow {self.player2} will go first.\n')
    
  
          
      
     

    
  
        