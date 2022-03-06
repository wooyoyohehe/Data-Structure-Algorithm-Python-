class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # format: [value, index]
        stack = []
        ans = [-1 for _ in range(len(nums))]
        for i in range(2*len(nums)):
            if i >= len(nums):
                i -= len(nums)
            if len(stack) == 0 or nums[i] <= stack[-1][0]:
                stack.append((nums[i], i))
            else:
                while stack and nums[i] > stack[-1][0]:
                    if stack[-1][1] < len(ans):
                        ans[stack[-1][1]] = nums[i]
                    stack.pop()
                stack.append((nums[i], i))
        return ans
                