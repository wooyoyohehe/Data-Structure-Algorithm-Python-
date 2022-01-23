class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = [-float('inf')]*3
        for num in nums:
            if num in temp:
                continue
            elif num > temp[2]:
                temp[0], temp[1], temp[2] = temp[1], temp[2], num
            elif num > temp[1]:
                temp[0], temp[1] = temp[1], num
            elif num > temp[0]:
                temp[0] = num
        if temp[0] != -float('inf'):
            return temp[0]
        else:
            return max(nums)