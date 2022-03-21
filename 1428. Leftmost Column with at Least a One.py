# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row, col):
#        """
#        :type row : int, col : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        row,col = binaryMatrix.dimensions()
        ans = col
        boundry = col-1
        for i in range(row):
            left = 0
            right = boundry
            if binaryMatrix.get(i, col-1) == 1:
                while left <= right:
                    mid = (left+right) //2
                    cur = binaryMatrix.get(i, mid)
                    if cur:
                        ans = min(ans, mid)
                        boundry = ans
                        right = mid - 1
                    else:
                        left = mid + 1
        return -1 if ans == col else ans
                        
                
                
                
                
                
                
                
                
                
                
                
        