class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        used = [[ 0 for _ in range(len(board[0]))] for _ in range(len(board))]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def helper(i, j, index):
            if word[index] != board[i][j]:
                return False
            if index == len(word)-1:
                return True
            result = False
            used[i][j] = 1
            for dir in directions:
                if 0 <= i+dir[0] < len(board) and 0 <= j+dir[1] < len(board[0]):
                    if used[i+dir[0]][j+dir[1]] == 0 :
                        if helper(i+dir[0], j+dir[1], index+1):
                            result = True
                            break
            used[i][j] = 0
            return result
           
        for i in range(len(board)):
            for j in range(len(board[0])):
                if helper(i, j, 0):
                    return True
        return False