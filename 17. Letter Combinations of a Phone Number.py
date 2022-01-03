class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        
        table = ["" , "", "abc", "def", "ghi", "jkl","mno", "pqrs","tuv","wxyz"]
        ans = [[]]
        for digit in table[int(digits[0])]:
            ans[0].append(digit)
        if len(digits) == 1:
            return ans[0]
        
        # in the given digit
        for i in range(1, len(digits)):
            ans.append([])
            for s1 in ans[i-1]:
            # in the current string 
                for s2 in table[int(digits[i])]:
                    # generate new strings old+new
                    ans[i].append(s1 + s2)
        return ans[-1]