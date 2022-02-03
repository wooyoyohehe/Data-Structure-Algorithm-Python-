class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def backtrack(s, path):
            if len(s) == 0:
                ans.append(path)
                return
            for i in range(1, len(s)+1):
                if s[:i] == s[:i][::-1]:
                    backtrack(s[i:], path + [s[:i]])
        ans = []
        backtrack(s, [])
        return ans