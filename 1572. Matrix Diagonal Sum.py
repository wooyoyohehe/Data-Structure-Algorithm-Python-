class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        ans = 0
        visited = set()
        for i in range(len(mat)):
            ans += mat[i][i]
            visited.add((i,i))
        for j in range(len(mat)-1, -1, -1):
            if (len(mat)-1-j, j) not in visited:
                ans += mat[len(mat)-1-j][j]
        return ans