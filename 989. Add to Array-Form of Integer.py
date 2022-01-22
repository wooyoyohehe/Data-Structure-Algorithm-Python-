class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        num2 = []
        while 1:
            num2 = [k%10] + num2
            k = k//10
            if k < 10:
                if k != 0:
                    num2 = [k] + num2
                break
        addition = 0
        if len(num) > len(num2):
            num2 = [0]*(len(num)-len(num2)) + num2
        else:
            num = [0]*(len(num2)-len(num)) + num
        ans = []
        for i in range(len(num)-1, -1, -1):
            if num[i] + num2[i] + addition > 9:
                ans = [num[i] + num2[i] + addition - 10] + ans
                addition = 1
            else:
                ans = [num[i] + num2[i] + addition] + ans
                addition = 0
        if addition == 1:
            ans = [1] + ans
        return ans