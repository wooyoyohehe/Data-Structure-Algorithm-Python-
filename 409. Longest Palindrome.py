class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = dict()
        ans = 0
        count = 0
        for ss in s:
            if ss not in dic:
                dic[ss] = 1
            else:
                dic[ss] += 1
        for key in dic:
            if dic[key]%2==0:
                ans += dic[key]
            else:
                if dic[key] != 1:
                    ans += dic[key]-1
                count+=1
        if count >= 1:
            return ans+1
        else:
            return ans