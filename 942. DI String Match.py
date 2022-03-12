class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        ans = []
        low = 0
        high = len(s)
        for ss in s:
            if ss == "I":
                ans.append(low)
                low+=1
            else:
                ans.append(high)
                high-=1
        return ans+[low]
                
        