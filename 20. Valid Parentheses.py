class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1:
            return False
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if c == ')' and stack[-1] == '(' or c == ']' and stack[-1] == '[' or c == '}' and stack[-1] == '{':
                        stack.pop()
                        continue
                return False
        return len(stack)==0