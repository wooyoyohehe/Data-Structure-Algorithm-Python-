class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        visited = [False]*len(nums)
        ans = []
        def backtrack(path):
            if len(path) == len(nums):
                ans.append(path)
                return
            for i in range(len(nums)):
                if visited[i]:
                    continue
                if i!=0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue
                visited[i] = True
                backtrack(path+[nums[i]])
                visited[i] = False
        backtrack([])
        return ans