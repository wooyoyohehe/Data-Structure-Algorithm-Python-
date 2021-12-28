class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        ans = ""
        for row in range(numRows):
            sign = -1
            i = 1
            index = 0
            while index < len(s):
                if i == numRows or i == 1:
                    sign = -sign
                if i == row+1:
                    ans += s[index]
                i += sign
                index += 1
        return ans
                