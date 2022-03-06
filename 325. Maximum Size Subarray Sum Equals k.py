class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix = dict()
        prefix[0] = -1
        ans = 0
        pre_sum = 0
        for i in range(len(nums)):
            pre_sum += nums[i]
            if pre_sum not in prefix:
                prefix[pre_sum] = i
            if pre_sum-k in prefix:
                ans = max(ans, i - prefix[pre_sum-k])
        return ans
            
            
        
        