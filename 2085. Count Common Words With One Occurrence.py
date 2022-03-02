class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        dic1 = dict()
        dic2 = dict()
        for word in words1:
            if word not in dic1:
                dic1[word] = 1
            else:
                dic1[word] += 1
        for word in words2:
            if word not in dic2:
                dic2[word] = 1
            else:
                dic2[word] += 1
        ans = 0
        for key in dic1:
            if dic1[key] == 1 and key in dic2 and dic2[key] == 1:
                ans += 1
        return ans
        