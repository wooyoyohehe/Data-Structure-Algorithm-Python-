class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)
        ans = ""
        for i in range(len(num)):
            if num[i] == "6":
                ans = ans + "9" + num[i+1:]
                return ans
            else:
                ans += "9"
        return ans