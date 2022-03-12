class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        cols = ord(s[3])-ord(s[0])+1
        for i in range(cols):
            for row in range(int(s[1]), int(s[4])+1):
                letter = chr(ord(s[0])+i)
                ans.append(chr(ord(s[0])+i)+str(row))
        return ans