class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        index = []
        for i in range(len(seats)):
            if seats[i] == 1:
                index.append(i)
        if len(index) == 1:
            return max(len(seats)-1-index[0], index[0])

        index = [-1] + index + [len(seats)]
        ans = -1
        for i in range(len(index)-1):
            if index[i] == -1 or index[i+1] == len(seats):
                closest = index[i+1]-index[i]-1
            else:
                closest = (index[i+1]-index[i]) // 2

            ans = max(closest,ans)
        return ans