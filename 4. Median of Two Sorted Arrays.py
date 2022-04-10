class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        """
        1,2
        |
        3,4
        |
        
        """
        
        i,j = 0,0
        length = len(nums1)+len(nums2)
        median1 = 0
        median2 = 0
        
        while i+j<=length//2:
            if i < len(nums1) and (j == len(nums2) or nums1[i] <= nums2[j]):
                i += 1
                if i+j == length//2:
                    median1 = nums1[i-1]
                if i+j == length//2+1:
                    median2 = nums1[i-1]
                    break
            elif j < len(nums2) and (i == len(nums1) or nums1[i] > nums2[j]):
                j += 1
                if i+j == length//2:
                    median1 = nums2[j-1]
                if i+j == length//2+1:
                    median2 = nums2[j-1]
                    break
        if length%2:
            return median2
        else:
            return (median1+median2)/2.0
                    
            


                
            
                    
            
            
        