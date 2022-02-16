class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def check(load):
            day, i, temp = 0, 0, 0
            while i < len(weights):
                temp += weights[i]
                if temp <= load:
                    i += 1
                else:
                    day += 1
                    temp = 0
            return day+1

        left, right, ans = max(weights), sum(weights), float("inf"), 
        while left <= right:
            mid = left + (right-left) // 2
            if check(mid) > days:
                left = mid+1
            else:
                ans = min(ans, mid)
                right = mid-1
        return ans