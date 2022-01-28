class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = {}
        ans = []
        for num in nums1:
            if num not in dic:
                dic[num] = 1
        for num in nums2:
            if  num in dic and num not in ans:
                ans.append(num)
        return ans