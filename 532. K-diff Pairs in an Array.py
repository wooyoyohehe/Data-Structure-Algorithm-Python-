class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        """
        [3,1,4,1,5]
         |
        dic = {1:[1,3], 
               3:[0], 
               4:[2], 
               5:[4]}
        ans = 2
        k = 2
        """
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 0
            dic[nums[i]]+=1
        ans = 0
        for key in dic:
            if key+k in dic and k != 0:
                ans += 1
            elif k == 0 and dic[key] > 1:
                ans += 1
        return ans
                
            
        