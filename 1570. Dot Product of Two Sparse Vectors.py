class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.values = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                self.values[i] = nums[i]
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        res = 0
        for key in self.values:
            if key in vec.values:
                res += self.values[key] * vec.values[key]
        return res
            
        
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)