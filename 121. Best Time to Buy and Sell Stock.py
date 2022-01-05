class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1:
            return 0
        if len(prices) == 2:
            if prices[0] >= prices[1]:
                return 0
            else:
                return prices[1]-prices[0]
        max_profit = 0
        history_min = prices[0]
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - history_min)   
            history_min = min(prices[i], history_min)
        return max_profit