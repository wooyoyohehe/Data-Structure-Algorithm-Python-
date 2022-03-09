class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        ans = 0
        for word in words:
            flag = True
            for w in word:
                if w not in allowed:
                    flag = False
                    break
            if flag:
                ans += 1
        return ans
            
        