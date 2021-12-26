class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits)-1
        number = 0
        co = 1
        while i>=0:
            number += digits[i] * co
            co*=10
            i-=1
        return [int(x) for x in str(number+1)]