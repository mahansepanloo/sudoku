


   
def Level():
    level = int(input("\n choose alevel between 1,2 and 3: "))

    while True:
        if level < 1 or level > 3:
            level = int(input("wrong\n choose alevel between 1,2 and 3: "))        
        else:
            break
        

   
    if level == 1:
        board = [[8, 0, 0, 9, 1, 3, 4, 0, 0],            
             [0, 4, 0, 0, 0, 7, 9, 0, 5],  
             [0, 9, 0, 2, 0, 0, 6, 0, 0],  
             [6,0, 0, 3, 0, 5, 0, 7, 0],  
             [1, 5, 0, 0, 2, 0, 3, 0, 9],  
             [3, 7, 0, 8, 9, 0, 0, 5, 0],  
             [4, 0, 7, 1, 0, 0, 0, 0, 0],  
             [0, 8, 0, 4, 7, 9, 0, 3, 0],  
             [9, 0, 0, 0, 3, 0, 0, 6, 4]]  
        
    elif level == 2:
        board = [[2, 0, 0, 0, 4, 0, 0, 5, 7],
             [0, 0, 1, 0, 0, 8, 0, 0, 0],
             [4, 0, 6, 0, 0, 0, 1, 3, 0],
             [0, 3, 5, 0, 0, 6, 0, 0, 0],
             [0, 7, 9, 4, 8, 5, 2, 1, 0],
             [0, 2, 4, 1, 3, 0, 6, 9, 5],
             [0, 0, 2, 7, 1, 0, 0, 0, 0],
             [0, 0, 0, 8, 0, 2, 0, 6, 1],
             [5, 0, 0, 0, 0, 0, 7, 0, 0]]
        
    elif level == 3:
        board  = [[0, 0, 0, 7, 0, 0, 0, 0, 0],
             [8, 0, 2, 0, 6, 9, 0, 0, 0],
             [0, 0, 5, 2, 8, 0, 0, 0, 0],
             [0, 0, 5, 2, 8, 0, 0, 0, 0],
             [0, 1, 3, 8, 0, 0, 5, 0, 9],
             [0, 0, 0, 0, 0, 0, 8, 0, 1],
             [0, 0, 4, 0, 1, 0, 6, 7, 0],
             [3, 7, 0, 9, 2, 0, 0, 0, 0],
             [4, 0, 9, 0, 0, 0, 0, 6, 0],
             [0, 0, 0, 3, 4, 0, 9, 0, 8]]
                          
    return board
def is_valid_move(board, row, col, num):  #اعتبار سنجی جدول 
    if num in board[row]:  #چک کردن سطر ها
        return False  

    if num in [board[i][col] for i in range(9)]:   #چک کردن ستون ها
        return False  

    
    block_col =  3 * (col // 3)  #چک کردن مربع  3*3
    block_row = 3 * (row // 3)

    if num in [  board[r][c]  for r in range(block_row, block_row + 3)  for c in range(block_col, block_col + 3) ]:  
        return False  
    return True  



def is_winner(board):  #چک کردن پیروزی
    for row in board:  
        if 0 in row:  
            return False  
    return True 


def iterbord(board):  
    for row in board:  
        print (row)

        
def play_sudoku():   # بازی 
    board=Level()
    print("\nEmpty Sudoku Board:")  
    iterbord(board)  
    while not is_winner(board):  
        row = int(input("Enter row number (1-9): ")) - 1  
        col = int(input("Enter column number (1-9): ")) - 1  
        num = int(input("Enter number to fill (1-9): ")) 
         
        if is_valid_move(board, row, col, num):  
            board[row][col] = num  
        else:  
            print(f"!!!!!!!!!!Invalid move.!!!!!!!!!!!!!!! The number {num}  in row *{row+1}* or column *{col+1}*. Please try again.")  
        print("Updated Sudoku Board:")  
        iterbord(board)  
    print("amazing! You have won the game!")  
play_sudoku()