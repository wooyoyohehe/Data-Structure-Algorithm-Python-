class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(string):
            count = 0
            for ss in string:
                if ss == "(":
                    count += 1
                elif ss == ")":
                    count -= 1
                    if count < 0:
                        return False
            return count == 0
        
        left, right = 0, 0
        for ss in s:
            if ss == "(":
                left += 1
            elif ss == ")":
                if left == 0:
                    right += 1
                else:
                    left -= 1
        ans = []
        visited = set()
        def backtrack(rest, l, r):
            if l == left and r == right and isValid(rest):
                ans.append(rest)
                return
            for i in range(len(rest)):
                if rest[i] in "()":
                    new_l = l
                    new_r = r
                    if rest[i] == "(":
                        new_l += 1
                    else:
                        new_r += 1
                    if new_l<=left and new_r<=right:
                        new_rest = rest[:i]+rest[i+1:]    
                        if new_rest not in visited:
                            visited.add(new_rest)
                            backtrack(new_rest, new_l, new_r)
        backtrack(s, 0, 0)
        return ans
                
        