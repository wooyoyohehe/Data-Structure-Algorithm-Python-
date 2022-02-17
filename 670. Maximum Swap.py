class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        number = []
        ans = num
        while num // 10 >= 0 and num != 0:
            number.append(num%10)
            num = num // 10
        number_s = sorted(number)
        for j in range(len(number)-1,-1,-1):
            if number[j] != number_s[j]:
                for k in range(len(number)):
                    if number[k] == number_s[j]:
                        number[k], number[j] = number[j], number[k]
                        ans = 0
                        weight = 1
                        l = 0
                        while l < len(number):
                            ans += number[l]*weight
                            weight*=10
                            l += 1
                        return ans
        return ans