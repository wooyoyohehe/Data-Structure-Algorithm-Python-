class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        results = [n]
        while 1:
            sum_ = 0
            for s in str(n):
                sum_ += int(s)*int(s)
            if sum_ == 1:
                return True
            else:
                if sum_ in results:
                    return False
                else:
                    results.append(sum_)
                    n = sum_