def helper(s, l, r):
    temp_start = l
    temp_len = 0
    while 1:
        if s[l] == s[r]:
            temp_len += 2
            temp_start = l
            l -= 1
            r += 1
        if l < 0 or r > len(s) - 1 or s[l] != s[r]:
            return temp_start, temp_len
        
class Solution(object):
    def longestPalindrome(self, s):

        if len(s) == 0:
            return None
        if len(s) == 1:
            return s
        if len(s) == 2 and s[0] == s[1]:
            return s
        if len(s) == 2 and s[0] != s[1]:
            return s[0]

        max_len = 1
        start = 0
        for i in range(1, len(s) - 1):
            temp_start, temp_len = helper(s, i - 1, i + 1)
            temp_len += 1
            if temp_len > max_len:
                start = temp_start
                max_len = temp_len

        for i in range(0, len(s) - 1):
            temp_start, temp_len = helper(s, i, i + 1)
            if temp_len > max_len:
                start = temp_start
                max_len = temp_len
        return s[start:start + max_len]