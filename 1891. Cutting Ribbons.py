class Solution(object):
    def maxLength(self, ribbons, k):
        """
        :type ribbons: List[int]
        :type k: int
        :rtype: int
        """
        min_possible = 1
        max_possible = max(ribbons)
        ans = 0
        while min_possible <= max_possible:
            cur = min_possible + (max_possible-min_possible)//2
            num = 0
            for ribbon in ribbons:
                num += ribbon//cur
            if num >= k:
                ans = max(cur, ans)
                min_possible = cur + 1
            else:
                max_possible = cur - 1
        return ans