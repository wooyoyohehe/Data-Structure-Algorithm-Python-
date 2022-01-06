class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        current = nums[0]
        for i in range(1, len(nums)):
            if current == nums[i]:
                count+=1
            else:
                count-=1
                if count == 0:
                    current = nums[i+1]
        return current