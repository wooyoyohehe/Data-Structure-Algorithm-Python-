class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums)):
            if index[i] >= len(ans):
                ans.append(nums[i])
            else:
                ans = ans[:index[i]] + [nums[i]] + ans[index[i]:]
        return ans
        