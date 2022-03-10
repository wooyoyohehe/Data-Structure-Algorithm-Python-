class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        visited = set(words)
        ans = []
        def helper(rest):
            for i in range(1, len(rest)):
                prefix = rest[:i]
                suffix = rest[i:]
                if prefix in visited and suffix in visited:
                    return True
                if prefix in visited and helper(suffix):
                    return True
            return False
        for word in words:
            if helper(word):
                ans.append(word)
        return ans