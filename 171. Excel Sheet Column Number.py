class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        ans = 0
        for i in range(len(columnTitle)):
            ans = ans*26 + ord(columnTitle[i])-ord("A")+1   
        return ans