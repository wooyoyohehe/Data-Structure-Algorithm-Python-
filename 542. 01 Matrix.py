class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    mat[i][j] = m+n
                    if 0<=i-1<m and 0<=j<n:
                        mat[i][j] = min(mat[i][j], mat[i-1][j]+1)
                    if 0<=i<m and 0<=j-1<n:
                        mat[i][j] = min(mat[i][j], mat[i][j-1]+1)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if mat[i][j] != 0:
                    if 0<=i+1<m and 0<=j<n:
                        mat[i][j] = min(mat[i][j], mat[i+1][j]+1)
                    if 0<=i<m and 0<=j+1<n:
                        mat[i][j] = min(mat[i][j], mat[i][j+1]+1)
        return mat