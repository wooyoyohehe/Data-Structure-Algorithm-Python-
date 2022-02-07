class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        dp = heights[-1]
        ans = [len(heights)-1]
        for i in range(len(heights)-2, -1, -1):
            if heights[i] > dp:
                ans.append(i)
            dp = max(dp, heights[i])
        return ans[::-1]