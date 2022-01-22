class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        left = 0
        right = len(s)-1
        s = list(s)
        while left<right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left] in vowels:
                right -= 1
            elif s[right] in vowels:
                left +=1
            else:
                right -= 1
                left += 1
        return ''.join(s)