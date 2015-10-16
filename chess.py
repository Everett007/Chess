# A program written in python for chess.
# Meant to be cross-platform.
# REMINDER: DO NOT USE SYSTEM OR PLATFORM INDEPENDANT FUNCTIONS OR MODULES!!!!!
# Made By:          Everett Daniels-Wright
# Version:          Alpha 0.1
# Important imports
import re
import math

# Global Constants ( Might be changed in the future to where people can choose their names )
player1 = 'Player 1'
player2 = 'Player 2'
first_player = player1
other_player = player2

# Global Variables
player_move = ''
board = [['R','H','B','K','Q','B','H','R'],
	 ['P','P','P','P','P','P','P','P'],
	 [' ',' ',' ',' ',' ',' ',' ',' '],
	 [' ',' ',' ',' ',' ',' ',' ',' '],
	 [' ',' ',' ',' ',' ',' ',' ',' '],
	 [' ',' ',' ',' ',' ',' ',' ',' '],
	 ['P','P','P','P','P','P','P','P'],
	 ['R','H','B','Q','K','B','H','R']]

# A cross-platform way to clear the screen
def cls():
  for i in range(0, 50):
    print ''

# A function to make a turn
def turn(player):
  print "%s, it's your turn. Make a move: " % player,
  player_move = str(raw_input()).lower()
  if re.search('^([abcdefgh][12345678]) to ([abcdefgh][12345678])$', player_move):
    pmc = re.search('^([abcdefgh][12345678]) to ([abcdefgh][12345678])', player_move)
    mp1 = pmc.group(1)
    mp2 = pmc.group(2)
    print mp1
    print mp2
  else:
    print 'Invalid! Your turn is skipped!'
  mp1 = mp1.split()
  mp2 = mp2.split()
  print mp1[0]
  print mp1[1]
  print mp2[0]
  print mp2[1]
    
# A function to print the board
def print_board():
    for i in range(0, 8):
        for j in range(0, 8):
            print board[i][j] + ' |',
        print ''

print_board()
turn(first_player)

