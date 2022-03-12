class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = []
        for num in range(left, right+1):
            digits = set()
            flag = True
            for s in str(num):
                digits.add(int(s))
            digits = list(digits)
            for digit in digits:
                if digit == 0 or num % digit != 0:
                    flag = False
                    break
            if flag:
                ans.append(num)
        return ans
                    
        