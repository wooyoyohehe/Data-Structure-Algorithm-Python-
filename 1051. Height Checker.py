class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        new_heights = sorted(heights)
        ans = 0
        for i in range(len(heights)):
            if new_heights[i] != heights[i]:
                ans += 1
        return ans
        