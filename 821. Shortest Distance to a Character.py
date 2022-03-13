class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        pos = []
        for i in range(len(s)):
            if s[i] == c:
                pos.append(i)
        ans = []
        for i in range(len(s)):
            if s[i] == c:
                ans.append(0)
            else:
                temp = 100001
                for p in pos:
                    temp = min(temp, abs(p-i))
                ans.append(temp)
        return ans
            
        