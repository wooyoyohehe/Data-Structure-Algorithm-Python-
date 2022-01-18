class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1 or x == 0:
            return x
        left = 0
        right = x
        mid = x//2
        ans = -1
        while left<=right:
            mid = (left+right)//2
            if mid*mid > x:
                right = mid-1
            if mid*mid <= x:
                ans = mid
                left = mid+1
        return ans