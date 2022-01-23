class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = [0] * (max(nums)+1)
        for i in range(len(nums)):
            hash_table[nums[i]] += nums[i]
        for i in range(2, len(hash_table)):
            hash_table[i] = max(hash_table[i-2]+hash_table[i], hash_table[i-1])
        return max(hash_table[-1],hash_table[-2])