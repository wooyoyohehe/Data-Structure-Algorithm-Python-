class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        left,right,ans = 0,0,0
        dic = dict()
        while right < len(s):
            if len(dic) <= 2:
                if s[right] not in dic:
                    dic[s[right]] = 1
                else:
                    dic[s[right]] += 1
                right += 1
            else:
                ans = max(ans, right-left-1)
                while len(dic) == 3:
                    dic[s[left]] -= 1
                    if dic[s[left]] == 0:
                        dic.pop(s[left])
                    left += 1
        if len(dic) == 3: 
            return max(ans, right-left-1)
        else:
            return max(ans, right-left)