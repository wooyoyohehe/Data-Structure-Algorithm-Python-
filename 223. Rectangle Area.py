class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """
        area1 = (ax2-ax1)*(ay2-ay1)
        area2 = (bx2-bx1)*(by2-by1)
        if ax1>=bx2 or ax2<=bx1 or ay1>=by2 or ay2<=by1:
            return area1+area2
        left = max(ax1, bx1)
        right = min(ax2, bx2)
        low = max(ay1, by1)
        high = min(ay2, by2)
        overlap = (right-left)*(high-low)
        area1 = (ax2-ax1)*(ay2-ay1)
        area2 = (bx2-bx1)*(by2-by1)
        return area1+area2-overlap
        