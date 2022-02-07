class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.size = size
        self.nums = []
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.nums) < self.size:   
            self.nums.append(val)
            return float(sum(self.nums))/len(self.nums)
        else:
            self.nums.pop(0)
            self.nums.append(val)
            return float(sum(self.nums))/self.size
            
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)