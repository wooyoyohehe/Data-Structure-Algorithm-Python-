class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 3:
            return sum(nums)
        result = 3001
        nums.sort()
        for left in range(len(nums)-2):
            middle = left+1
            right = len(nums)-1
            while middle < right:
                sum_ = nums[left]+nums[right]+nums[middle]
                if sum_ == target:
                    return target
                elif sum_ > target:
                    right-=1
                elif sum_ < target:
                    middle+=1
                if abs(sum_ - target) < abs(result - target):
                        result = sum_
        return result
                    