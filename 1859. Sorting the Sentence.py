class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(" ")
        temp = [""]*len(s)
        for i in range(len(s)):
            temp[int(s[i][-1])-1] = s[i][:-1]
        return " ".join(temp)