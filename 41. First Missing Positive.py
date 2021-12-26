class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i<len(nums):
            if nums[i] == i+1 or nums[i] <= 0 or nums[i]>len(nums) or nums[nums[i]-1] == nums[i]:
                i+=1
            else:
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
        for j in range(len(nums)):
            if nums[j] != j+1:
                return j+1
        return len(nums)+1