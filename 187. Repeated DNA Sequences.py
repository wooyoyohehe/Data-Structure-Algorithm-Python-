class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        dic = {}
        for i in range(len(s)-9):
            if s[i:i+10] in dic and s[i:i+10] not in ans:
                ans.append(s[i:i+10])
            else:
                dic[s[i:i+10]] = 1
        return ans