class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums[0] == 0 and len(nums) != 1:
            return False
        if len(nums) == 1:
            return True

        cur = 0
        cur_max = nums[0]
        while cur_max < len(nums)-1:
            if cur > cur_max:
                return False
            else:
                cur_max = max(cur + nums[cur], cur_max)
                cur += 1
        return True