# TIC TAC TOE

from random import randrange


def tictactoe_game():
    cpu_retry = True
    coins = 0
    move_count = 0 # va da 5 a 10
    human_com = 0
    cpu_com = 0
    board = [
        [0, 0, 0], 
        [0, 0, 0], 
        [0, 0, 0]
            ]

    board_logic = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2)
    }

    board[1][1] = "X" # PC first move
    cpu_com += 1
    move_count = 1
    human_retry = False
    row = 01
    
    col = 0

    while coins == 0:
        coins = int(input("INSERT 1 COIN TO START A NEW GAME: "))
    else:
        try:
            human_com = int(input("Make your move [1 - 9]: "))
            while board[row][col] == "X": 
                human_com = int(input("Make your move [1 - 9]: ")) 
            else:
                for _ in board_logic:
                    row, col = board_logic[human_com] # PRENDO I,J DELLA BOARD

                board[row][col] = "O" # GLI METTO O NELLA POSIZIONE SCELTA DALL UMANO
                move_count += 1
                print("Human Moved")

                while cpu_retry == True:
                    row, col = board_logic[cpu_com] 
                    if board[row][col] == "X":
                        cpu_retry = True
                        print("CPU insert - Position Used")
                        cpu_com = randrange(8)
                    else:
                        cpu_retry = False
                        board[row][col] = "X"
                        move_count += 1
                        print("CPU Moved")
                        if move_count == 9:
                                return

        except(ValueError, TypeError):
            print("Please put only integer value from 1 to 9 to make your move!")

                
            
    print(board)

    
tictactoe_game()   





