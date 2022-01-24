class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return False
        ans = 0
        for i in range(1, int(num**0.5+1)):
            if num % i == 0:
                ans += i
                ans += num/i
        return ans/2 == num