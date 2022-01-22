# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while 1:
            mid = left + (right-left) // 2 
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                right = mid - 1
            elif guess(mid) == 1:
                left = mid + 1