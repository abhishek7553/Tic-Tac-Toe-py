from colorama import *

def check_game(current_game):
    diags_1=[]
    diags_2=[]
    for i in range(len(current_game)):
        diags_1.append(current_game[i][i])
        diags_2.append(current_game[i][-(i+1)])
    
    if diags_1.count(diags_1[0])==len(diags_1) and diags_1[0]!=0:
        print(f"Player {diags_1[0]} is a WINNER diagonally!!!")
        return True
    
    if diags_2.count(diags_2[0])==len(diags_2) and diags_2[0]!=0:
        print(f"Player {diags_2[0]} is a WINNER anti-diagonally!!!")
        return True


    for col in range(len(current_game)):
        check=[]

        for row in current_game:
            check.append(row[col])

        if check.count(check[0])==len(check) and check[0]!=0:
            print(f"Player {check[0]} is a WINNER vertically!!!")
            return True   


    for row in current_game:
        if row.count(row[0])== len(row) and row[0]!=0:
            print(f"Player {row[0]} is a WINNER horizontally!!!")
            return True

    return False

def game_map(game,player=0,row=0,column=0,just_display=False):
 
    try:
        if not just_display:
            if game[row][column] == 0:
                game[row][column]=player
            else:
                print("This positision is already ocupied, choose another!!")
                return game,False
            

        print("   " + "  ".join([str(i) for i in range(len(game))]))

        for count,rows in enumerate(game):
            col_row=""
            for item in rows:
                if item == 0:
                    col_row+="   "
                elif item == 1:
                    col_row+=Fore.GREEN + ' X ' + Style.RESET_ALL
                elif item == 2:
                    col_row+=Fore.RED + ' O ' + Style.RESET_ALL
            print(count,col_row)

        return game,True    

    except IndexError as e:
        print("ERROR : make sure to input co-ordinates as ")
        print("   " + "  ".join([str(i) for i in range(len(game))]))
        print(e)
        return game,False
    except Exception as e:
        print("SOMETHING IS WRONG!!!")
        return game,False

player=[1,2]
play=True
while play:
    game_size=int(input("What size of tic-tac-toe game do you want? :"))
    game_board = [[0 for i in range(game_size)]for i in range(game_size)]
    print("\t\t\tTIC-TAC-TOE")
    game_won=False
    current_player=1
    game_board, _ =game_map(game_board,just_display=True)
    while not game_won:
        print(f"\nPLAYER {current_player} CHANCE:")
        played=False
        while not played:
            column_choice = int(input("WHAT COLUMN DO YOU WANNA PLAY? : "))
            row_choice = int(input("WHAT ROW DO YOU WANNA PLAY? : "))
            game_board,played = game_map(game_board,player=current_player,row=row_choice,column=column_choice)

        current_player=player[current_player%2]
        if check_game(game_board):
                print("\nGAME OVER!")
                game_won=True

    x=int(input("DO YOU WANT PLAY AGAIN? (1 , 0) :"))
    if not x:
        play=False