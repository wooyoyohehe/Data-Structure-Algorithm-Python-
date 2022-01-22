class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        ans = 5001
        while left <= right:
            mid = left +(right-left)//2
            ans = min(ans, nums[mid])
            if nums[mid] == nums[left] and nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[mid] > nums[right]:
                left = mid + 1       
            else:
                right = mid - 1
        return ans