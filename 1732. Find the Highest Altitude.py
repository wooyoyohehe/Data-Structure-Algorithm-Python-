class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        h = 0
        ans = 0
        for g in gain:
            h += g
            ans = max(ans, h)
        return ans