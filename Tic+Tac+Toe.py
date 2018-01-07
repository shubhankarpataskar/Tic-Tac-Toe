
# coding: utf-8

# In[1]:


from __future__ import print_function 


# In[2]:


from IPython.display import clear_output
def display_board(board):
    clear_output()
    print("   |   |  ")
    print(" "+board[7]+" | "+board[8]+" | "+board[9])
    print("   |   |  ")
    print('-----------')
    print("   |   |  ")
    print(" "+board[6]+" | "+board[5]+" | "+board[4])
    print("   |   |  ")
    print('-----------')
    print("   |   |  ")
    print(" "+board[3]+" | "+board[2]+" | "+board[1])
    print("   |   |  ")


# In[3]:


def player_input():
    marker = ''
    while not(marker == 'O' or marker == 'X'):
        marker =  input('Do you want to be X or O:').upper()
        if marker == 'X':
            return('X','O')
        else:
            return('O','X')


# In[4]:


def place_marker(board, marker, position):
    board [position] = marker
    


# In[5]:


def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
            (board[6] == mark and board[5] == mark and board[4] == mark) or
            (board[3] == mark and board[2] == mark and board[1] == mark) or
            (board[7] == mark and board[6] == mark and board[3] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or 
            (board[9] == mark and board[4] == mark and board[1] == mark) or
            (board[3] == mark and board[5] == mark and board[9] == mark) or
            (board[7] == mark and board[5] == mark and board[1] == mark))


# In[6]:


import random
def choose_first():
    if random.randint(0,1) == 0:
        return ('Player 1')
    else:
        return ('Player 2')
    


# In[7]:


def space_check(board, position):
    return (board[position] == ' ')


# In[8]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


# In[9]:


def player_choice(board):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board,int(position)):
        position = input('Choose your next position in-between (1-9)')
    return int(position)


# In[10]:


def replay():
    return (input('Do you want to play again? :').lower().startswith('y'))


# In[11]:


print('Welcome to Tic Tac Toe!')

while True:
    theboard = [' ']*10
    p1_marker,p2_marker = player_input()
    turn = choose_first()
    print (turn + ' Will play first!')
    
    game_on = True
    
    while game_on:
        if turn == 'Player 1':
            
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard,p1_marker,position)
            
            if win_check(theboard,p1_marker):
                display_board(theboard)
                print('Player 1 wins!')
                game_on = False
                
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print("It's a Draw!")
                    break
                
                else:
                    turn = 'Player 2'
        else:
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard,p2_marker,position)
            
            if win_check(theboard,p2_marker):
                display_board(theboard)
                print('Player 2 wins!')
                game_on = False
                
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print("It's a Draw!")
                    break
                
                else:
                    turn = 'Player 1'
    if not replay():
        break  
              
    

