from datetime import datetime




def Level():
    level = int(input("choose alevel between 1,2 and 3: "))       
    while True:
        if level < 1 or level > 3:
            level = int(input("wrong\n choose alevel between 1,2 and 3: "))        
        else:
            break
        
    # if level == 0:  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      برای تست کردنه ردیف 9 ستون 9 اگه 9 بزاری بازی تموم میشه      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #     board = [[5,3,4,6,7,8,9,1,2],            
    #              [6,7,2,1,9,5,3,4,8],  
    #              [1,9,8,3,4,2,5,6,7],  
    #              [8,5,9,7,6,1,4,2,3],  
    #              [4,2,6,8,5,3,7,9,1],  
    #              [7,1,3,9,2,4,8,5,6],  
    #              [9,6,1,5,3,7,2,8,4],  
    #              [2,8,7,4,1,9,6,3,5],
    #              [3,4,5,2,8,6,1,7,0]]
   
    if level == 1:
        board = [[8, 0, 0, 9, 1, 3, 4, 0, 0],            
                 [0, 4, 0, 0, 0, 7, 9, 0, 5],  
                 [0, 9, 0, 2, 0, 0, 6, 0, 0],  
                 [6, 0, 0, 3, 0, 5, 0, 7, 0],  
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
        # print(f"row!!!{board[row].index(num)+1}")
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
        yield (row)

def solve(board = None, row = None, col = None):

    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0
    if board[row][col] > 0:
        return solve(board, row, col + 1)
   
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):

            board[row][col] = num

            if solve(board, row, col + 1):
                return True
       
        board[row][col] = 0
    return False

board = Level()

if solve(board, 0, 0):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()
else:
    print("No Solution")

