class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 1
        right = num
        while left <= right:
            i = left + (right-left) // 2
            if i*i == num:
                return True
            elif i*i < num:
                left = i + 1
            elif i*i > num:
                right = i - 1
        return False