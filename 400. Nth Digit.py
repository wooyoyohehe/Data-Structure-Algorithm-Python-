class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit = 1
        nums = 9
        prev = 0
        while n - digit*nums > 0:
            n -= digit*nums
            prev = digit
            digit += 1
            nums *= 10
        if n % digit == 0:
            return int(str(10 ** prev + n//digit - 1)[n % digit-1])
        else:
            return int(str(10 ** prev + n//digit)[n % digit-1])