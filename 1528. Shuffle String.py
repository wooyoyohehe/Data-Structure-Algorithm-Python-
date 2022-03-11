class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        dic = {}
        for i in range(len(s)):
            dic[indices[i]] = s[i]
        ans = ""
        for i in range(len(s)):
            ans += dic[i]
        return ans
            