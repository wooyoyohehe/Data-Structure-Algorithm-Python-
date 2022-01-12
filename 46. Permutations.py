class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]
        result = []
        def helper(rest, result, path):
            if len(path) == len(nums):
                result.append(path)
                return
            for i in range(len(rest)):
                helper(rest[:i]+rest[i+1:], result, path + [rest[i]])
        helper(nums, result, [])
        return result