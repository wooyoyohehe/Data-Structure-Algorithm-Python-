class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        ans = ""
        num_ = abs(num)
        count = 0
        while num_ != 0:
            ans = str(num_ % 7) + ans
            count += 1
            num_ = num_//7
        if num >= 0:
            return ans
        else:
            return "-" + ans