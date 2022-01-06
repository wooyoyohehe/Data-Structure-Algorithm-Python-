class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        up = 0
        down = len(matrix)-1
        if len(matrix) == 1:
            row = 0
        else:
            while up <= down:
                mid = (up+down) // 2
                if matrix[mid][-1] == target:
                    return True
                elif matrix[mid][-1] < target:                  
                    up = mid+1
                elif matrix[mid][-1] > target:
                    if matrix[mid][0] <= target:
                        break
                    else:
                        down = mid-1
            row = mid
        mid = 0
        left = 0 
        right = len(matrix[0])-1
        while left <= right:
            mid = (left+right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:                  
                left = mid + 1
            elif matrix[row][mid] > target:
                right = mid - 1
        return False