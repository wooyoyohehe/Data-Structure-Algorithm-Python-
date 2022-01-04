class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        left = 0
        right = len(nums)-1
        while nums[right] == 2:
            right -= 1
            if right == -1:
                return nums
        while left != right:
            if nums[left] == 2:
                nums[left] = nums[right]
                nums[right] = 2
                right -= 1
            else:
                left += 1
                
                
        while nums[right] != 0:
            right -= 1
            if right == -1:
                return nums
        left = 0
        while left != right:
            if nums[left] == 1:
                nums[left] = nums[right]
                nums[right] = 1
                right -= 1
            else:
                left += 1
        return nums