class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return str(int(str(num)[::-1]))[::-1] == str(num)