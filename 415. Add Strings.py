class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        addition = 0
        if len(num1) > len(num2):
            num2 = "0"*(len(num1)-len(num2)) + num2
        else:
            num1 = "0"*(len(num2)-len(num1)) + num1
        digit_num = max(len(num1), len(num2))
        ans = ""
        for i in range(digit_num-1, -1, -1):
            if int(num1[i])+int(num2[i])+addition > 9:
                ans = str(int(num1[i])+int(num2[i])+addition - 10) + ans
                addition = 1
            else:
                ans = str(int(num1[i])+int(num2[i])+addition) + ans
                addition = 0
        if addition == 1:
            ans = "1" + ans
        return ans

