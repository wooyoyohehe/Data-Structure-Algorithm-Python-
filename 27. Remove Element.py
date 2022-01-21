class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            if nums[0] == val:
                return 0
            else:
                return 1
        pointer = 0
        while pointer != len(nums):
            if nums[pointer] == val:
                nums.pop(pointer)
            else:
                pointer += 1
        return len(nums)