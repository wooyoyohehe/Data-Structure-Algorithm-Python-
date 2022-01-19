class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        ans = 0
        for num in nums:
            if num not in dic:
                dic[num] = 1
                if num - 1 in dic:
                    dic[num] += dic[num-1]
                if num + 1 in dic:
                    dic[num] += dic[num+1]
                ans = max(ans, dic[num])
                left = num - 1
                right = num + 1
                while left in dic:
                    dic[left] = dic[num]
                    left -= 1
                while right in dic:
                    dic[right] = dic[num]
                    right += 1
        return ans