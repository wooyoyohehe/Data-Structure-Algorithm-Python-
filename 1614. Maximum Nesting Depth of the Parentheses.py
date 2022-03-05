class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp, ans = 0, 0
        for ss in s:
            if ss == "(":
                temp += 1
                ans = max(ans, temp)
            elif ss == ")":
                temp -= 1
        return ans