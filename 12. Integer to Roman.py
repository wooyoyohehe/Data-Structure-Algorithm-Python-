class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ""
        
        if num//1000 != 0:
            for i in range(num // 1000):
                ans += "M"
            num = num % 1000
        if num//100 != 0:
            if 1 <= num // 100 <= 3:
                ans += (num // 100) * "C"  
            elif num // 100 == 4:
                ans += "CD"
            elif 5 <= num // 100 <= 8:
                ans += "D"
                ans += (num // 100 - 5) * "C"
            elif num // 100 == 9:
                ans += "CM"
            num = num % 100
        if num//10 != 0:
            if 1 <= num // 10 <= 3:
                ans += (num // 10) * "X"  
            elif num // 10 == 4:
                ans += "XL"
            elif 5 <= num // 10 <= 8:
                ans += "L"
                ans += (num // 10 - 5) * "X"
            elif num // 10 == 9:
                ans += "XC"
            num = num % 10
        
        if num == 4:
            return ans+"IV"
        if num == 9:
            return ans+"IX"
        if 0<=num<=3:
            return ans+"I"*num
        if 5<= num <=8:
            return ans+"V"+"I"*(num-5)