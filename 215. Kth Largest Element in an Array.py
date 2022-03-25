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

import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # quickselect
        # partition and select
        # 1. pivot
        # 2. compare and swap
        # 3. update the real pos of pivot
        # 4. put pivot at the real pos
        # 5. if pos == n-k, return pivot
        # 6. if pos < n-k, go right
        # 7. if pos < n-k, go left

        pos = 0
        left = 0
        right = len(nums)-1
        pivot = 0
        while 1:
            pos = left
            pivot = nums[left]
            nums[left], nums[right] = nums[right], nums[left]
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[i], nums[pos] = nums[pos], nums[i]
                    pos += 1
            nums[pos], nums[right] = nums[right], nums[pos]
            if pos == len(nums)-k:
                return pivot
            elif pos < len(nums)-k:
                left = pos+1
            else:
                right = pos-1
                
                
        