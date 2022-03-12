class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        dic = {}
        ans = set()
        for num in nums1:
            if num not in dic:
                dic[num] = 1
        for num in nums2:
            if num not in dic:
                dic[num] = 2
            else:
                if dic[num] != 2:
                    ans.add(num)
        for num in nums3:
            if num not in dic:
                dic[num] = 3
            else:
                if dic[num] != 3:
                    ans.add(num)
        return list(ans)
        