class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        prefix = [0]*(len(nums)+1)
        dic = dict()
        dic[0] = -1
        for i in range(len(nums)):
            prefix[i+1] = prefix[i] + nums[i]
            remainder = prefix[i+1] % k
            if remainder in dic:
                if i - dic[remainder] >= 2:
                    return True
            else:
                dic[remainder] = i
        return False