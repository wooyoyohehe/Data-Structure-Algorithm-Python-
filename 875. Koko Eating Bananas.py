import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def check(speed):
            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile)/speed)
            return hours
        
        ans = float("inf")
        left = 1
        right = max(piles)
        while left <= right:
            mid = left+ (right-left)//2
            if check(mid) <= h:
                ans = min(ans, mid)
                right = mid-1
            else:
                left = mid+1
        return ans