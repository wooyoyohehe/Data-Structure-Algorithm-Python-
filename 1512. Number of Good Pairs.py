class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = dict()
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        ans = 0
        for key in dic:
            if dic[key] > 1:
                ans += dic[key]*(dic[key]-1)/2
        return ans
        