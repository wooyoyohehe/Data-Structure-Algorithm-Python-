class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        left = 0
        right = 0
        while right < len(s):
            while right < len(s) and s[right] != " ":
                right += 1
            start = right
            right -= 1
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            right = left = start + 1