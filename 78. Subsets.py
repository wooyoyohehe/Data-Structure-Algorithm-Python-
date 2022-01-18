class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        ans = []
        for i in range(2**n):
            binary = bin(i)[2:].zfill(n)
            temp = []
            for j in range(n):
                if binary[j] == "1":
                    temp.append(nums[j])
            ans.append(temp)
        return ans