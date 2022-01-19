class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans = []
        board = [["." for _ in range(n)] for _ in range(n)]

        def check(board, row, column):
            for i in range(n):
                if board[i][column] == "Q":
                    return False
            i = row-1
            j = column-1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1
            i = row - 1
            j = column + 1
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1
            return True

        def backtrack(row,board,temp,ans):
            temp_list = []
            if row == n:
                for each_line in board:
                    temp = ''.join(each_line)
                    temp_list.append(temp)
                ans.append(temp_list)
                return
            for i in range(n):
                if not check(board, row, i):
                    continue
                board[row][i] = "Q"
                backtrack(row+1, board, temp+[[row,i]], ans)
                board[row][i] = "."
        backtrack(0, board,[],ans)
        return ans