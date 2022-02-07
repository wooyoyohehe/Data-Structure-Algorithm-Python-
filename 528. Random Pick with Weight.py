class Solution:

    def __init__(self, w: List[int]):
        self.ranges = []
        range_ = 0
        for weight in w:
            range_ += weight
            self.ranges.append(range_)
        self.total_sum = range_
        

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()
        left, right = 0, len(self.ranges)-1
        while left < right:
            mid = left+(right-left)//2
            if target > self.ranges[mid]:
                left = mid+1
            else:
                right = mid
        return left
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()