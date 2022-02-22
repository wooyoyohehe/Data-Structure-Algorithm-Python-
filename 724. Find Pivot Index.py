class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        temp = 0
        nums = [0] + nums + [0]
        for i in range(1, len(nums)-1):
            if temp == float(total-nums[i]) / 2:
                return i-1
            else:
                temp += nums[i]
        return -1