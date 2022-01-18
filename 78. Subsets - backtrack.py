def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    ans = []
    def backtrack(ans, index, path):
        ans.append(path)
        for i in range(index, len(nums)):
            backtrack(ans, i+1, path+[nums[i]])
    backtrack(ans, 0, [])
    return ans
nums = [1,2,3]
print(subsets(nums))