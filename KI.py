import random 
import board

def make_random_move(brettMatrix: list): # Wählt zufällig ein leeres Feld für den Zug der KI.
    position = random.randint(0,8)
    if board.check_if_valid(brettMatrix, position):
        return position
    else:
        return brettMatrix.index('     ')
    
    
def make_good_move(brettMatrix: list):
    for combo in board.winning_combinations:
        computer = sum(1 for i in combo if 'O' in brettMatrix[i] and isinstance(i, int) and 0 <= i < 9)
        spieler = sum(1 for i in combo if brettMatrix[i] == '  X  'and isinstance(i, int) and 0 <= i < 9)
        
        # Wenn der Computer in diese Kombination gewinnen kann 
        if computer == 2 and spieler == 0:
            for i in combo:
                #assert isinstance(i, int)
                #assert 0 <= i < 9
                if brettMatrix[i] == '     ':
                    return i  # Geben den Index zurück
         
                
    for combo in board.winning_combinations:
        computer = sum(1 for i in combo if 'O' in brettMatrix[i] and isinstance(i, int) and 0 <= i < 9)
        spieler = sum(1 for i in combo if brettMatrix[i] == '  X  'and isinstance(i, int) and 0 <= i < 9)
        #  Wenn der Spieler in diese Kombination gewinnen kann
        if spieler == 2 and computer == 0:
            for i in combo:
                #assert isinstance(i, int)
                #assert 0 <= i < 9
                if brettMatrix[i] == '     ':
                    return i  # Geben den Index zurück
        #Wenn es keine ander Variante gibt
        
    for combo in board.winning_combinations:
        computer = sum(1 for i in combo if 'O' in brettMatrix[i] and isinstance(i, int) and 0 <= i < 9)
        spieler = sum(1 for i in combo if brettMatrix[i] == '  X  'and isinstance(i, int) and 0 <= i < 9)
        
        # Wenn der Computer in diese Kombination gewinnen kann 
        if computer == 1 and spieler == 0:
            for i in combo:
                #assert isinstance(i, int)
                #assert 0 <= i < 9
                if brettMatrix[i] == '     ':
                    return i  # Geben den Index zurück    
                       
    return make_random_move(brettMatrix) 

'''brettMatrix = ['  O  ', '  X  ', '  X  ',
              '     ', '     ', '  X  ',
              '  O  ', '     ', '     '] 

print(make_good_move(brettMatrix))'''