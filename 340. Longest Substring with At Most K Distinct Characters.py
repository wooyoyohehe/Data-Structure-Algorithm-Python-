class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0
        left,right,ans = 0,0,0
        dic = dict()
        while right < len(s):
            dic[s[right]] = right
            right += 1
            if len(dic) == k+1:
                idx = min(dic.values())
                dic.pop(s[idx])
                left = idx+1
            ans = max(ans, right-left)
        return ans
