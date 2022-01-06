def helper(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left+right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return -1

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1:
            if nums[0] != target:
                return -1
            else:
                return 0
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] > nums[-1]:
                result = helper(nums[:mid+1],target)
                if result != -1:
                    return result
                else:
                    left = mid +1     
            else:
                result = helper(nums[mid:],target)
                if result != -1:
                    return result + mid
                else:
                    right = mid - 1
        return -1