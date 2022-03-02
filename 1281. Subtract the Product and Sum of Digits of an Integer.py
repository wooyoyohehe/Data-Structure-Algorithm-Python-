class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = []
        while n // 10 != 0:
            digits = [n%10] + digits
            n = n //10
        digits = [n%10] + digits
        product = 1
        sum_ = 0
        for i in range(len(digits)):
            sum_ += digits[i]
            product *= digits[i]
        return product-sum_