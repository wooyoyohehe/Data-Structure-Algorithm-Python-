class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]
        if len(nums) == 1 and nums[0] != target:
            return [-1, -1]
        if target < nums[0] or target > nums[-1]:
            return [-1,-1]
        left = 0
        right = len(nums)-1
        while 1:
            if left == right and nums[left] == target:
                return [left, left]
            if left == right and nums[left] != target:
                return [-1, -1]
            mid = (left+right) // 2
            if nums[mid] == target:
                begin = end = mid
                while begin >= 1:
                    if nums[begin-1] != target:
                        break
                    else:
                        begin -= 1
                while end <= len(nums)-2:
                    if nums[end+1] != target:
                        break
                    else:
                        end += 1
                return [begin, end]
            if nums[mid] < target:
                left = mid+1
                continue
            if nums[mid] > target:
                right = mid-1
                continue
        return [-1, -1]
        
        