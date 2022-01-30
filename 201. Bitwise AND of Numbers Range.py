class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if len(bin(left)) != len(bin(right)):
            return 0
        else:
            ans = left
            for i in range(left+1,right+1):
                ans = ans & i
            return ans