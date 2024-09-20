# TIC TAC TOE

from random import randrange
1,9
def tictactoe_game():
    coins = 0
    human_command = 0
    
    board = {
        1:"0", 2:"0", 3:"0",
        4:"0", 5:"0", 6:"0",
        7:"0", 8:"0", 9:"0"
    }

    available_moves = list(board.values()).count("0")
    random_move = 0

    while coins <= 0:
        coins = int(input("INSERT 1 COIN TO START A NEW GAME: "))
    else:
        print("##########","###GAME###","###START##","##########",sep="\n" )
        board[5] = "X" # PC first move
        
        # Stampa la scacchiera 3x3
        for i in range(1, 10, 3):
            print(board[i], board[i+1], board[i+2])
        
        while available_moves > 0: # se ci sta almeno uno spazio vuoto sulla board
            human_command = int(input("Make your move [1 - 9]: "))

            # manca verifica se 3 valori sono di file per fare tris

            for i in board:
                if(board[i] == "X"): # se all'indice troviamo una X e quell'indice è uguale alla mossa del H - riprova
                    if(i == human_command):
                        print("Used Position - Human Retry")
                    elif 9 > human_command <= 0:
                        print("Bad Input - from 1 to 9 please")
                    else:
                        # Human move
                        board.update({human_command:"O"})
                        print(f"Human make his move: {human_command}")
                        
                        # CPU RANDOM MOVE
                        random_move = randrange(1,9)

                        # UPDATE AVAILABLE MOVES NUMBER
                        available_moves = list(board.values()).count("0")

                        while i == random_move or human_command == random_move:
                            print("Used Position - CPU RETRY")
                            random_move = randrange(1,9)
                        else:
                            board.update({random_move:"X"})
                            available_moves = list(board.values()).count("0")
                            print(f"CPU make his move: {random_move}")
                    print("MOVES LEFT: ", available_moves)
        print("##########","###GAME###","###OVER###","##########",sep="\n" )
    
                
    
tictactoe_game()   





