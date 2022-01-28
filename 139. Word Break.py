class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        ans = [False]
        def helper(s,memo):
            if s in wordDict:
                ans[0] = True
                return
            for word in wordDict:
                if s[:len(word)] == word and s[len(word):] not in memo:
                    memo.append(s[len(word):])
                    helper(s[len(word):],memo)
        helper(s,[])
        return ans[0]