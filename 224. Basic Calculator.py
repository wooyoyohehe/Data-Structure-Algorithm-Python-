class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [1]
        i = 0
        sign = 1
        ans = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
            elif "0" <= s[i] <= "9":
                number = 0
                while i < len(s) and "0" <= s[i] <= "9":
                    number = number * 10 + ord(s[i]) - ord('0')
                    i += 1
                ans += number * sign
            elif s[i] == "(":
                i += 1
                stack.append(sign)
            elif s[i] == ")":
                i += 1
                stack.pop()
            elif s[i] == "+":
                i += 1
                sign = stack[-1]
            elif s[i] == "-":
                i += 1
                sign = -stack[-1]
        return ans

            


        