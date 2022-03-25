class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        max_freq = 0
        max_key = 0
        for num in nums:
            if num not in dic:
                dic[num] = 1         
            else:
                dic[num]+=1
            max_freq = max(dic[num], max_freq)
        temp = []
        for key in dic:
            if dic[key] == max_freq:
                temp.append(key)
        ans = float("inf")
        for num in temp:
            i = 0
            j = len(nums)-1
            while nums[i] != num:
                i += 1
            while nums[j] != num:
                j -= 1
            ans = min(ans, j-i+1)
        return ans
                
        