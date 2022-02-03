class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for p in s:
            if len(stack) == 0 or p == "(":
                stack.append(p)
            elif p == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(p)
        return len(stack)