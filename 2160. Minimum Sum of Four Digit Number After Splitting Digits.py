class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = []
        for digit in str(num):
            digits.append(int(digit))
        digits.sort()
        return digits[0]*10+digits[2]+digits[1]*10+digits[3]