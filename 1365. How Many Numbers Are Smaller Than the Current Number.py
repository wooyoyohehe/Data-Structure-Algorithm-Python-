class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        dic = {}
        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in dic:
                dic[sorted_nums[i]] = i
        for i in range(len(nums)):
            nums[i] = dic[nums[i]]
        return nums
                
        