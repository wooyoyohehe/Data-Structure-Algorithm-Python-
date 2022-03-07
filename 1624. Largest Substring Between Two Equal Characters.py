class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        visited = set()
        ans = -1
        for i in range(len(s)):
            if s[i] not in visited:
                j = len(s) - 1
                while j > i:
                    if s[j] == s[i]:
                        ans = max(ans, j-i-1)
                        break
                    j -= 1
                visited.add(s[i])
        return ans
                
        