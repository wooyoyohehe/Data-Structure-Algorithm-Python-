class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        factors = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                factors.append(i)
        half = []
        for i in range(len(factors)-1, -1, -1):
            if n != factors[i] * factors[i]:
                half.append(n//factors[i])
        factors = factors + half
        if k > len(factors):
            return -1
        else:
            return factors[k-1]
        