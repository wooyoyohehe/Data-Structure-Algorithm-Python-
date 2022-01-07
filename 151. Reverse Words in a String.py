class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        hehe = []
        for aa in s.split(" "):
            if aa != "":
                hehe.append(aa)
        return " ".join(hehe[::-1])