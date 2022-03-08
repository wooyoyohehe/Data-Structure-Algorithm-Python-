class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        left_x = max(rec1[0], rec2[0])
        right_x = min(rec1[2], rec2[2])
        bottom_y = max(rec1[1], rec2[1])
        top_y = min(rec1[3], rec2[3])
        return left_x < right_x and bottom_y < top_y
        