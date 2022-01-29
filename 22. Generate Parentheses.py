class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def helper(temp, left, right, ans):
            if left < right or left > n or right > n:
                return 
            if left == n and right == n:
                ans.append(temp)
                return 
            helper(temp+"(", left+1, right, ans)
            helper(temp+")", left, right+1, ans)
        helper("", 0, 0, ans)
        return ans