def uniquePathsWithObstacles(obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        ans = []
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        def helper(path, num_D, num_R):
            if num_D >= m or num_R >= n:
                return
            if num_D == m-1 and num_R == n-1:
                ans.append(path)
                return
            for direction in ["D", "R"]:
                if direction == "D":
                    helper(path+direction, num_D+1, num_R)
                else:
                    helper(path+direction, num_D, num_R+1)
        helper("", 0, 0)
        return ans
print(uniquePathsWithObstacles([[0,0,0],[0,0,0],[0,0,0]]))
