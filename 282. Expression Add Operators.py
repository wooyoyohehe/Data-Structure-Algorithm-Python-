class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        ans = []
        def backtrack(i, exp, result, mul):
            if len(num) == i:
                if result == target:
                    ans.append(''.join(exp))
                return
            value = 0
            sign_index = len(exp)
            if i > 0:
                exp.append("")
            for j in range(i, len(num)):
                if num[i] == "0" and j > i:
                    break
                value = value*10+int(num[j])
                exp.append(num[j])
                if i == 0:
                    backtrack(j+1, exp, value, value)
                else:
                    exp[sign_index] = "+"
                    backtrack(j+1, exp, result+value, value)
                    exp[sign_index] = "-"
                    backtrack(j+1, exp, result-value, -value)
                    exp[sign_index] = "*"
                    backtrack(j+1, exp, result-mul+mul*value, mul*value)
            del exp[sign_index:]
        backtrack(0,[],0,0)
        return ans
                  

                
            
        