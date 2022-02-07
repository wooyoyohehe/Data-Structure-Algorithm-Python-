class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        m = len(mat)
        n = len(mat[0])
        ans = []
        for idx in range(m):
            temp = []
            i = idx
            j = 0
            while 0 <= i < m and 0<= j < n:
                temp.append(mat[i][j])
                i -= 1
                j += 1
            if idx % 2 == 1:
                temp = temp[::-1]
            ans+= temp
        for idx in range(1, n):
            temp = []
            i = m-1
            j = idx
            while 0<= i < m and 0 <= j < n:
                temp.append(mat[i][j])
                i -= 1
                j += 1
            if m % 2 == idx % 2:
                temp = temp[::-1]
            ans+=temp
        return ans