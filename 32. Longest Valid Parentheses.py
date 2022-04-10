class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        """
        two pointers
        """
        left, right, ans = 0, 0, 0
        for i in range(len(s)):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if right == left:
                ans = max(ans, left*2)
            elif right > left:
                left, right = 0, 0
        left, right = 0, 0   
        for i in range(len(s)-1, -1, -1):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if right == left:
                ans = max(ans, right*2)
            elif left > right:
                left, right = 0, 0
        return ans
        
        
        
        
        
        
        """
        solution of stack: O(n) and O(n)
        stack = [-1]
        ans = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i-stack[-1])
        return ans
        """
        