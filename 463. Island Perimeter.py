class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    side = 0
                    if i == 0:
                        side += 1
                    if i == len(grid)-1:
                        side += 1
                    if j == 0:
                        side += 1
                    if j == len(grid[0])-1:
                        side += 1
                    if 0 < i and grid[i-1][j] == 0:
                        side += 1
                    if i < len(grid) - 1 and grid[i+1][j] == 0:
                        side += 1
                    if 0 < j and grid[i][j-1] == 0:
                        side += 1
                    if j < len(grid[0]) - 1 and grid[i][j+1] == 0:
                        side += 1
                    ans += side
        return ans