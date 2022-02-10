class Solution(object):
    def confusingNumber(self, n):
        """
        :type n: int
        :rtype: bool
        """
        new_num = ""
        n = str(n)
        for digit in n[::-1]:
            if digit not in "01869":
                return False
            elif digit in "018":
                new_num+=digit
            else:
                if digit == "6":
                    new_num+="9"
                else:
                    new_num+="6"
        return new_num != n