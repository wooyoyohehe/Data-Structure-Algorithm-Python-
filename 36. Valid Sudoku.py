class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row =[[ 0 for _ in range(10)] for _ in range(9)]
        column = [[ 0 for _ in range(10)] for _ in range(9)]
        sub_box = [[[0]*10 for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                else:
                    number = int(board[i][j])
                    row[i][number] += 1
                    column[j][number]+=1
                    sub_box[i//3][j//3][number] += 1
                    if row[i][number] > 1 or  column[j][number]>1 or sub_box[i//3][j//3][number]>1:
                        return False
        return True
