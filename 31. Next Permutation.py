class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        largest_l = -1
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                largest_l = i-1
                break
        if largest_l != -1:
            min_right = 101
            right = len(nums)-1
            while right > largest_l:
                if nums[largest_l] < nums[right] < min_right:
                    min_right = nums[right]
                    right_index = right
                right -= 1
            nums[largest_l], nums[right_index] = nums[right_index], nums[largest_l]

        while 1:
            flag = 0
            for i in range(largest_l+1, len(nums)-1):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    flag = 1
            if flag == 0:
                break