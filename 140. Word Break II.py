class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        ans = []
        def helper(rest, prev):
            if not rest:
                ans.append(prev[:-1])
                return
            for word in wordDict:
                if len(word) > len(rest):
                    continue
                if rest[:len(word)] == word:
                    new_prev = prev + word + " "
                    helper(rest[len(word):], new_prev)               
        helper(s, "")
        return ans