class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num // 10 == 0:
            return num
        ans = num
        while ans // 10 != 0:
            num = ans
            ans = 0
            while num != 0:
                ans += num%10
                num = num // 10
        return ans