class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        max_ = 0
        while left<right:
            max_ = max(max_, min(height[left], height[right])*(right-left))
            if height[left] > height[right]:
                right-=1
            else:
                left+=1
        return max_