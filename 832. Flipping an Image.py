class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = 1
        while right < len(s)//2+1:
            if s[left] == s[right]:
                if len(s) % (right-left) == 0:
                    if len(s) // (right-left) * s[left:right] == s:
                        return True
            right += 1
        return False