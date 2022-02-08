class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append([i, "("])
            elif s[i] == ")":
                if len(stack) == 0 or stack[-1][1] == ")":
                    stack.append([i, ")"])
                else:
                    stack.pop()
        s = list(s)
        for j in range(len(stack)-1, -1 , -1):
            s.pop(stack[j][0])
        return "".join(s)