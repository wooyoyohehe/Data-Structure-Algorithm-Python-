class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        ans = ""
        i = 0
        j = 0
        while j < len(s):
            if s[j] == "(":
                stack.append("(")
            else:
                stack.pop()
            if not stack:
                ans += s[i+1:j]
                i = j+1
            j += 1
        return ans