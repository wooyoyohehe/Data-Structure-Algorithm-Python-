class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [[False for _ in range(n)] for _ in range(n)]

        def check(board, row, column):
            for i in range(n):
                if board[i][column]:
                    return False
            i = row-1
            j = column-1
            while i >= 0 and j >= 0:
                if board[i][j]:
                    return False
                i -= 1
                j -= 1
            i = row - 1
            j = column + 1
            while i >= 0 and j < n:
                if board[i][j]:
                    return False
                i -= 1
                j += 1
            return True

        def backtrack(row,board):
            if row == n:
                return 1
            ans = 0
            for i in range(n):
                if not check(board, row, i):
                    continue
                board[row][i] = True
                ans += backtrack(row+1, board)
                board[row][i] = False
            return ans
        return backtrack(0, board)