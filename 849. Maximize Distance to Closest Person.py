class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        ans = -1
        left = -1
        for i in range(len(seats)):
            if seats[i] == 1:
                right = i
                if left == -1:
                    closest = right-left-1
                    ans = max(closest,ans)
                    left = right
                else:
                    closest = (right-left) // 2
                    ans = max(closest,ans)
                    left = right
            if i == len(seats) - 1:
                closest = i - right
                ans = max(closest,ans)
        return ans