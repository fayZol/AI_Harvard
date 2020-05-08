"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    number_of_X = 0
    number_of_O = 0
    
    for row in board:  
        number_of_X += row.count("X")
        number_of_O += row.count("O")
        
    
    if number_of_X <= number_of_O:
        return("X") 
    else: 
        return("O")


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions=set()
    
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                actions.add((i,j))
                
    return actions


#def result(board, action):
#    """
#    Returns the board that results from making move (i, j) on the board.
#    """
#    
#    board2 = copy.deepcopy(board)
#    possible_actions = actions(board)
#    if action not in possible_actions:
#        raise AttributeError
#    else:
#        board2[action[0]][action[1]] = player(board)     
#    
#    return board2

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board2 = copy.deepcopy(board)    
    possible_actions = actions(board)
    if action not in possible_actions:
        raise AttributeError
    else:
        board2[action[0]][action[1]] = player(board)     
    
    return board2


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    possible_wins = []
    row1 = board[0]
    row2 = board[1]
    row3 = board[2]
    col1 = [board[0][0],board[1][0],board[2][0]]
    col2 = [board[0][1],board[1][1],board[2][1]]
    col3 = [board[0][2],board[1][2],board[2][2]]
    diag1 = [board[0][0],board[1][1],board[2][2]]
    diag2 = [board[2][0],board[1][1],board[0][2]]
    
    possible_wins.append(row1)
    possible_wins.append(row2)
    possible_wins.append(row3)
    possible_wins.append(col1)
    possible_wins.append(col2)
    possible_wins.append(col3)
    possible_wins.append(diag1)
    possible_wins.append(diag2)
    
    for trait in possible_wins:
        if trait.count("X") == 3:
            return "X"
        elif trait.count("O") == 3:
            return "O"
    
    return None

    
#    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or len(actions(board)) == 0:
        return True
    else:
        return False
    
#    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    if winner(board) == 'X':
        return 1
    elif winner(board) == 'O':
        return -1
    else :
        return 0
#    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if terminal(board):
        return None
    else:
        if len(actions(board)) == 9:
            for action in actions(board):
                return action
        else:
            if player(board) == 'X':
                v = max_value(board)
                for action in actions(board):
                    if v == min_value(result(board, action)):
                        return action
            if player(board) == 'O':
                v = min_value(board)
                for action in actions(board):
                    if v == max_value(result(board, action)):
                        return action               
            
    
def max_value(board):
    if terminal(board):
        return utility(board)
    
    v = float("-inf")
    for action in actions(board):
        d = min_value(result(board, action))  
        v = max(v,d)
    return v

def min_value(board):
    
    if terminal(board):
        return utility(board)
    
    v = float("inf")
    for action in actions(board):
        d = max_value(result(board, action))
        v = min(v,d)

    return v
    
#    raise NotImplementedError
