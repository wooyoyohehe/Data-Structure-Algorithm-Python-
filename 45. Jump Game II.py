class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        if nums[0] >= len(nums)-1:
            return 1
        cur_index = 0
        step = 0
        reach = -1
        next_index = -1
        while reach < len(nums)-1:
            for i in range(cur_index+1, cur_index+nums[cur_index]+1):
                if nums[i] + i > reach:
                    reach = nums[i] + i
                    next_index = i
            step += 1
            cur_index = next_index
        step += 1
        return step