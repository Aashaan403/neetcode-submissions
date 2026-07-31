class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row check
        
        for row  in range(9):
            check = defaultdict(int)
            for col in range(9):
              if board[row][col].isnumeric() == True :
                check[board[row][col]] += 1
                if check[board[row][col]] >=1:
                    return False

        for row  in range(9):
            check = defaultdict(int)
            for col in range(9):
              if board[col][row].isnumeric():
                check[board[col][row]] += 1
                if check[board[col][row]] >=1:
                    return False
        return True
        m=0
        n=0
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row check
        
        for row  in range(9):
            check = defaultdict(int)
            for col in range(9):
              if board[row][col].isnumeric() == True :
                check[board[row][col]] += 1
                if check[board[row][col]] >1 :
                    return False

        for row  in range(9):
            check = defaultdict(int)
            for col in range(9):
              if board[col][row].isnumeric():
                check[board[col][row]] += 1
                if check[board[col][row]] >1:
                    return False

       

        m=0
        n=0
        for row in range(0,9,3):
            for col in range(0,9,3):
                check = set()
                for i in range(row,row+3):
                    for j in range(col,col+3):
                        if board[i][j] == ".":
                            continue
                        else:
                            if board[i][j] in check:
                                return False
                            else:
                                check.add(board[i][j])
        return True



                
        

       
        
        
                       
        

       
        
        
        