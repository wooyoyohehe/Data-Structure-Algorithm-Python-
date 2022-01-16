class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """ 
        m = len(matrix)
        n = len(matrix[0])
        ans = []

        start = 0
        if min(m,n) % 2 == 0:
            circle = min(m,n) // 2
        else:
            circle = min(m,n) // 2 + 1
        for _ in range(circle):
            if n - 2*start == 1:
                for i in range(m - 2*start):
                    ans.append(matrix[start+i][start])
                return ans
            if m - 2*start == 1:
                for i in range(n - 2*start):
                    ans.append(matrix[start][start+i])
                return ans
            for i in range(start, n-start-1):
                ans.append(matrix[start][i])
            for j in range(start, m-start-1):
                ans.append(matrix[j][n-start-1])
            for k in range(n-start-1, start, -1):
                ans.append(matrix[m-start-1][k])
            for l in range(m-start-1, start, -1):
                ans.append(matrix[l][start])
            start += 1
        return ans