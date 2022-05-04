class Solution(object):
    def largestUniqueNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 0
            dic[num] += 1
        ans = -1
        for key in dic:
            if key > ans and dic[key] == 1:
                ans = key
        return ans
            
        