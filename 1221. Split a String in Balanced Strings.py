class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        ans = 0
        for i in range(len(s)):
            if len(stack) == 0 or stack[-1] == s[i]:
                stack.append(s[i])
            else:
                stack.pop()
                if len(stack) == 0:
                    ans += 1
        return ans
                    
        