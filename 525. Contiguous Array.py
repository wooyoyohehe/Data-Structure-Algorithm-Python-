class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {0:-1}
        prefix = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                prefix -= 1
            else:
                prefix += 1
            if prefix not in dic:
                dic[prefix] = i
            ans = max(ans, i-dic[prefix])
        return ans
        
        
                
        