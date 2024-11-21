import board as b
import KI
import time
    
brettMatrix = b.brettMatrix
spieler1Score = 0
spieler2Score = 0
win = False
print('Player X')
spieler1 = input('Your name: ')
print('Player O')
spieler2 = 'Conputer'
print(spieler2)
move = ' '
current_player = spieler1
current_move = 'X'
you_want = 'y'
b.clear_terminal()
while you_want == 'y':
    while not win:
        b.headband(spieler1)
        b.draw_board(b.brettMatrix)
         
        if current_player == spieler1:
            while True:
                try:
                    position = int(input(f"{current_player}, where do you want to play? [0-8] "))
                    if b.is_right_position(position):
                        break
                        print("Invalid position. Please enter a number between 0 and 8.")
                except ValueError:
                    print("Invalid input. Please enter a valid number between 0 and 8.")
        else:
            position = KI.make_good_move(b.brettMatrix)   
        
        b.clear_terminal()
        
        if b.check_if_valid(b.brettMatrix, position):
            brettMatrix = b.make_move(position, current_move, b.brettMatrix)
        
            if b.check_win_condition(b.brettMatrix, current_move):
                b.draw_board(b.brettMatrix)
                print(f"Player {current_player} has won!")
                if current_player == spieler1:
                    spieler1Score += 1
                else:
                    spieler2Score += 1    
                break
            if b.is_board_full(b.brettMatrix):
                b.draw_board(b.brettMatrix)
                print("It's a draw! No more moves left.")
                break
            # Swap players
            
            if current_player == spieler1:
                current_player = spieler2
                current_move = 'O'
            else:
                current_player = spieler1
                current_move = 'X'
        else:
            print("Invalid position. Try again.")
    you_want =input('Do you want one more time? (y / n) ') 
    b.brettMatrix = ['     ' for _ in range(9)]
    b.clear_terminal()
           
            
b.score_board(spieler1, spieler2, spieler1Score, spieler2Score)  