class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = bin(x)[2:]
        y = bin(y)[2:]
        if len(x) > len(y):
            y = (len(x) - len(y)) * "0" + y
        else:
            x = (len(y) - len(x)) * "0" + x
        ans = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                ans+=1
        return ans