import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        q = []
        for num in nums:
            if len(q) == k:
                heapq.heappushpop(q, num)
            else:
                heapq.heappush(q, num)
        return heapq.heappop(q)