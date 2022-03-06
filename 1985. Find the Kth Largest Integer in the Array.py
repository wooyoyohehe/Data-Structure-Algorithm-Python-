class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        q = []
        for num in nums:
            if len(q) < k:
                heapq.heappush(q, int(num))
            else:
                heapq.heappushpop(q, int(num))
        return str(heapq.heappop(q))
                
            
        