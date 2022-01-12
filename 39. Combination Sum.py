class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(nums, target, path, result):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return

            for i in range(len(nums)):
                backtrack(nums[i:], target-nums[i], path+[nums[i]] ,result)

        result = []
        backtrack(candidates, target, [], result)
        return result