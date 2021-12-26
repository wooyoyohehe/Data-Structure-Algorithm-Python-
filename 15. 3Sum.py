class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 2:
            return []
        nums.sort()
        result = []
        for left in range(len(nums)-2):
            if left > 0 and nums[left] == nums[left-1]:
                continue
            right = len(nums)-1
            middle = left+1
            while middle<right:
                sum_ = nums[left]+nums[middle]+nums[right]
                if sum_ == 0:
                    if [nums[left],nums[middle],nums[right]] not in result:
                        result.append([nums[left],nums[middle],nums[right]])
                    middle+=1
                    continue
                elif sum_<0:
                    middle+=1
                elif sum_>0:
                    right-=1
        return result
                