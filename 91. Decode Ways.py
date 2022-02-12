class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1

        dp = [1] + [0]*(len(s)-1)
        if 10<= int(s[:2]) <= 26:
            dp[1] += 1
        if s[0] != "0" and s[1] != "0":
            dp[1] += 1
        for i in range(2, len(s)):
            if 10 <= int(s[i-1:i+1])<=26:
                dp[i] += dp[i-2]
            if s[i] != "0":
                dp[i] += dp[i-1]
        return dp[-1]