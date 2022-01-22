class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        ans = nums[0]
        while left <= right:
            mid = left +(right-left)//2
            ans = min(nums[mid], ans)
            if ans > nums[left] and ans < nums[right]:
                return nums[left]
            elif ans > nums[right]:
                left = mid + 1       
            else:
                right = mid - 1
        return ans