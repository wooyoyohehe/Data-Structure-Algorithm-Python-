class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left) // 2
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            elif nums[mid] != nums[mid-1]:
                if mid % 2 == 0:
                    left = mid + 1
                else:
                    right = mid-1
            else:
                if mid % 2 == 0:
                    right = mid-1
                else:
                    left = mid + 1
        return nums[left]