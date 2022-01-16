class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        ans = p = -1
        for i in range(len(seats)):
            if seats[i] == 1:
                if p == -1:
                    ans = max(i-1-p,ans)
                else:
                    ans = max((i-p) // 2,ans)
                p = i
        ans = max(len(seats) - 1 - p,ans)
        return ans