class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted(nums, key = lambda n: (nums.count(n), -n) )