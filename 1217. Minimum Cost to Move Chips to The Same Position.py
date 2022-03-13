class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        odd = 0
        even = 0
        for pos in position:
            if pos%2:
                odd += 1
            else:
                even += 1
        return min(odd,even)
        