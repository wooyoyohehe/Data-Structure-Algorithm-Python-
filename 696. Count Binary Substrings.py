class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 1
        ans = 0
        while right < len(s):
            if s[left] != s[right]:
                count = 1
                l = left-1
                r = right+1
                while l>=0 and s[l]==s[left] and r<len(s) and s[r] == s[right]:
                    count += 1
                    l -= 1
                    r += 1
                ans += count
            left += 1
            right += 1
        return ans
                