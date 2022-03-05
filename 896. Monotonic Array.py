class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        flag = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if flag == -1:
                    return False
                flag = 1
            elif nums[i] < nums[i+1]:
                if flag == 1:
                    return False
                flag = -1
        return True
                
            
            
            