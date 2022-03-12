class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        box = [0 for _ in range(50)]
        for i in range(lowLimit, highLimit+1):
            temp = 0
            while i > 0:
                temp += i%10
                i = i//10
            box[temp] += 1
        return max(box)