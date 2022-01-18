class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        def backtrack(ans, index, path):
            ans.append(path)
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                backtrack(ans, i+1, path+[nums[i]])
        backtrack(ans, 0, [])
        return ans