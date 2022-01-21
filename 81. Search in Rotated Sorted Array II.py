class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] == nums[left] and nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[mid] >= nums[left]:
                if target < nums[left] or target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] <= nums[right]:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return False