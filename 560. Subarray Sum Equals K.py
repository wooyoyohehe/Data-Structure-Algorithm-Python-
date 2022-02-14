class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = dict()
        dic[0] = 1
        pre_sum = [0]*(len(nums)+1)
        count = 0
        for i in range(len(nums)):
            pre_sum[i+1] = pre_sum[i]+nums[i]
            if pre_sum[i+1] - k in dic:
                count += dic[pre_sum[i+1] - k]
            if pre_sum[i+1] not in dic:
                dic[pre_sum[i+1]] = 1
            else:
                dic[pre_sum[i+1]] += 1
        return count