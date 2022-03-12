class Solution(object):
    def sumOfDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = min(nums)
        sum_ = 0
        while num > 0:
            sum_ += num%10
            num = num//10
        return abs(sum_%2-1)
        