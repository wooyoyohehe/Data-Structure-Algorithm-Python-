class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        stack = []
        Sign = '+'
        num = ""
        for i in range(n):
            if "0" <= s[i] <= "9":
                num += s[i]
            if i == n - 1 or s[i] in '+-*/':
                if Sign == '+':
                    stack.append(int(num))
                elif Sign == '-':
                    stack.append(-int(num))
                elif Sign == '*':
                    stack.append(stack.pop() * int(num))
                else:
                    temp = stack.pop()
                    if temp < 0:
                        stack.append(-int(-temp / int(num)))
                    else:
                        stack.append(int(temp / int(num)))
                Sign = s[i]
                num = ""
        return sum(stack)