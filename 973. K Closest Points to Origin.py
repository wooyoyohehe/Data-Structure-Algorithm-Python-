def helper(e):
        return e[0]*e[0]+e[1]*e[1]
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        points.sort(key = helper)
        return points[:k]
    