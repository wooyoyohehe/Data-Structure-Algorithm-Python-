class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prices.append(10001)
        stack = []
        ans = 0
        length = 0
        for price in prices:
            if not stack or price - stack[-1] == -1:
                stack.append(price)
                length += 1
            else:
                ans += length*(length+1) // 2
                stack = [price]
                length = 1
        return ans
        