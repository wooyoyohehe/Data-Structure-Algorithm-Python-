class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = ""
        for ss in s:
            if 'a' <= ss <= 'z' or '0' <= ss <= '9':
                new_s += ss
            if 'A' <= ss <= 'Z':
                new_s += ss.lower()
                
        if len(new_s) == 0 or len(new_s) == 1:
            return True
        left = 0
        right = len(new_s)-1
        while left<right:
            if new_s[left] != new_s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True