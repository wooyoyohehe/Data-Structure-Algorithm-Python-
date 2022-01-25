class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        element1 = nums[0]
        count1 = 0
        element2 = nums[0]
        count2 = 0
        for i in range(len(nums)):
            if nums[i] == element1:
                count1 += 1
            elif nums[i] == element2:
                count2 += 1
            else:
                if count1 == 0:
                    element1 = nums[i]
                    count1 = 1
                    continue
                if count2 == 0:
                    element2 = nums[i]
                    count2 = 1
                    continue
                else:
                    count1 -= 1
                    count2 -= 1
        count1 = 0
        count2 = 0
        ans = []
        for num in nums:
            if num == element1:
                count1 += 1
            if num == element2:
                count2 += 1
        if count1 > len(nums)//3:
            ans.append(element1)
        if count2 > len(nums)//3 and element1 != element2:
            ans.append(element2)
        return ans