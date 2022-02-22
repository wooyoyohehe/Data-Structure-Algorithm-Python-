class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def isValid(i,j,num):
            for k in range(9):
                if board[i][k] == num:
                    return False
                if board[k][j] == num:
                    return False
            # check the 3*3 block
            for m in range(i//3*3, i//3*3+3):
                for n in range(j//3*3, j//3*3+3):
                    if num == board[m][n]:
                        return False
            return True
                
        def backtrack(i, j):
            if j == 9:
                return backtrack(i+1,0)
            if i == 9:
                return True
            if board[i][j] != ".":
                return backtrack(i,j+1)
            for num in ["1","2","3","4","5","6","7","8","9"]:
                if isValid(i,j,num):
                    board[i][j] = num
                    if backtrack(i,j+1):
                        return True
                    board[i][j] = "."
            return False
        backtrack(0,0)
            
        