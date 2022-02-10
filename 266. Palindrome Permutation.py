class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = dict()
        for ss in s:
            if ss not in dic:
                dic[ss] = 1
            else:
                dic[ss] += 1
        count = 0
        for key in dic:
            if dic[key]%2 == 1:
                count+=1
        return count <= 1