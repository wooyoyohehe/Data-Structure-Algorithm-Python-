class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        dic = {}
        max_len = 0
        for rec in rectangles:
            length = min(rec)
            if length >= max_len:
                if length not in dic:
                    dic[length] = 1
                else:
                    dic[length] += 1
                max_len = length
        return dic[max_len]