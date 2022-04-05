class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        ans = 0
        while num1 and num2:
            if num1 > num2:
                ans += num1//num2
                num1 = num1%num2
            else:
                ans += num2//num1
                num2 = num2%num1
        return ans
            
        