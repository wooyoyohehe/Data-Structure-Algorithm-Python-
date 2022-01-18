class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        left = start = 0
        for i in range(len(gas)):
            if left + gas[i] - cost[i] < 0:
                start = i+1
                left = 0
            else:
                left = left + gas[i] - cost[i]
        return start
