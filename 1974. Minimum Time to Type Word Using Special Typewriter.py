class Solution(object):
    def minTimeToType(self, word):
        """
        :type word: str
        :rtype: int
        """
        word = "a" + word
        ans = 0
        for i in range(1, len(word)):
            dis = abs(ord(word[i])-ord(word[i-1]))
            ans += min(dis+1, 27-dis)
        return ans