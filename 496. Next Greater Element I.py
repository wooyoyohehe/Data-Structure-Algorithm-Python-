class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # [1,3,4,2,0,7]
        stack = []
        dic = {}
        for i in range(len(nums2)):
            if len(stack) == 0 or nums2[i] < stack[-1]:
                stack.append(nums2[i])
            if nums2[i] > stack[-1]:
                while stack and nums2[i] > stack[-1]:
                    dic[stack[-1]] = nums2[i]
                    stack.pop()
                stack.append(nums2[i])
        for item in stack:
            dic[item] = -1
        ans = []
        for num in nums1:
            ans.append(dic[num])
        return ans
            
                