class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n == 1:
            return
        start = 0
        rotate_time = n-1
        while rotate_time>0:
            for i in range(rotate_time):
                matrix[start][i+start], matrix[i+start][n-1-start], matrix[n-1-start][n-1-i-start], matrix[n-1-i-start][start] = matrix[n-1-i-start][start],matrix[start][i+start], matrix[i+start][n-1-start], matrix[n-1-start][n-1-i-start]
            start += 1
            rotate_time -= 2