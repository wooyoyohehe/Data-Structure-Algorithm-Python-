class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            row_min = min(matrix[i])
            min_index = matrix[i].index(row_min)
            col_max = 0
            for j in range(m):
                col_max = max(col_max, matrix[j][min_index])
            if col_max == row_min:
                ans.append(col_max)
        return ans
                
        