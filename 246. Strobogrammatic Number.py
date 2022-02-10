class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        new_num = ""
        for digit in num[::-1]:
            if digit not in "01869":
                return False
            elif digit in "018":
                new_num+=digit
            else:
                if digit == "6":
                    new_num+="9"
                else:
                    new_num+="6"
        return new_num == num