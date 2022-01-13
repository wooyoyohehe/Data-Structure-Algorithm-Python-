class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                right = stack.pop()
                left = stack.pop()
                if token == "+":
                    stack.append(left+right)
                    continue
                if token == "-":
                    stack.append(left-right)
                    continue
                if token == "*":
                    stack.append(left*right)
                    continue
                if token == "/":
                    if left*right<0:
                        stack.append(-(abs(left)//abs(right)))
                    else:
                        stack.append(left//right)
            else:
                stack.append(int(token))
        return stack[0]