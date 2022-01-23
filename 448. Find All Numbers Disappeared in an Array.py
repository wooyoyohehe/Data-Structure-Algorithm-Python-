class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        nums = [0] + nums
        while p < len(nums):
            if nums[p] != p:
                if nums[p] != nums[nums[p]]:
                    nums[nums[p]], nums[p] = nums[p], nums[nums[p]]
                else:
                    nums[p] = 0
                    p += 1
            else:
                p += 1
        ans = []
        for i in range(1,len(nums)):
            if nums[i] == 0:
                ans.append(i)
        return ans