class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]
        result = []
        visited = [0]*len(nums)
        
        def helper(result, path):
            if len(path) == len(nums):
                result.append(path)
                return
            nums.sort()
            for i in range(len(nums)):
                if visited[i] == 1:
                    continue
                if i!=0 and nums[i] == nums[i-1] and visited[i-1]==0:
                    continue
                visited[i] = 1
                helper(result, path+[nums[i]])
                visited[i] = 0
        helper(result, [])
        return result