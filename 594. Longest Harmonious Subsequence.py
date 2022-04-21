class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        ans = 0
        for num in nums:
            if num not in dic:
                dic[num] = 0
            dic[num] += 1
        for key in dic.keys():
            if key+1 in dic:
                ans = max(ans, dic[key]+dic[key+1])
        return ans
            
            
            