import os
brettMatrix = ['     ', '     ', '     ',
              '     ', '     ', '     ',
              '     ', '     ', '     '] 
winning_combinations = [
        [0, 1, 2],  # Rows
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6], # Columns
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8], # Diagonals
        [2, 4, 6]
    ]

def draw_board(brettMatrix: list): #Zeichnet die aktuelle Spielposition.   
    print()
    print()
    print(f"{brettMatrix[0]}|{brettMatrix[1]}|{brettMatrix[2]}")
    print("-----|-----|-----")
    print(f"{brettMatrix[3]}|{brettMatrix[4]}|{brettMatrix[5]}")
    print("-----|-----|-----")
    print(f"{brettMatrix[6]}|{brettMatrix[7]}|{brettMatrix[8]}")
    print()
    print()
    print('--------------------------------') 
    
def headband(name:str):
    print('--------------------------------') 
    print('Player X')
    print(f'Name: {name}')
    print('Player O')
    print('Conputer') 
    print('--------------------------------') 
        
def score_board(spieler1, spieler2, spieler1Score, spieler2Score):            
    print('--------------------------------')         
    print('-----------SCOREBOARD-----------')   
    print('--------------------------------')     
    print(f'{spieler1:<10}         {spieler1Score:^10}')
    print(f'{spieler2:<10}         {spieler2Score:^10}')
    print('--------------------------------')
    
def check_if_valid(brettMatrix, position): #Überprüft, ob ein Zug möglich ist.
    if brettMatrix[position] == '     ':
        return True
    else:
        return False    
    
def check_win_condition(brettMatrix, move):# Prüft, ob ein Spieler gewonnen hat oder das Spiel unentschieden endet.

    for combo in winning_combinations:
        
        if all(brettMatrix[i] == f'  {move}  ' for i in combo):
            return True
        
    return False    

    
def clear_terminal(): # Löscht das Terminal.
    os.system('cls' if os.name == 'nt' else 'clear')
    

def make_move(position, move, brettMatrix): # Update the board with 'X' or 'O'
    brettMatrix[position] = f'  {move}  '
    return brettMatrix
    
def is_board_full(brettMatrix): #Prüft, ob ein Position noch verfügt ist.
    if '     ' not in brettMatrix:
        return True    
    
def is_right_position(position):
    if isinstance(position, int):
        if 0 <= position <= 8:
            return True    
        else:
            return False
    else:
        return False