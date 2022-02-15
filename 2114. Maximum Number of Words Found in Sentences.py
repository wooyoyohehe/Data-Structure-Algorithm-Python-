class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        ans = 0
        for sen in sentences:
            ans = max(ans, len(sen.split(" ")))
        return ans
        