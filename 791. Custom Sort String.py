class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        dic = {}
        remain = ""
        for alpha in order:
            dic[alpha] = []
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]].append(i)
            else:
                remain += s[i]
        temp = ""
        for alpha in order:
            temp += alpha*len(dic[alpha])
        return temp+remain