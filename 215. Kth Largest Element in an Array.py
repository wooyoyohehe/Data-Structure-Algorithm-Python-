class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        heap = []
        for hehe in nums:
            if count >= k:
                heapq.heappush(heap, hehe)
                heapq.heappop(heap)
            else:
                heapq.heappush(heap, hehe)
                count += 1
        return heap[0]

  