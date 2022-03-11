class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        s1 = s1.split()
        s2 = s2.split()
        dic1 = dict()
        dic2 = dict()
        for s in s1:
            if s not in dic1:
                dic1[s] = 1
            else:
                dic1[s] += 1
        for s in s2:
            if s not in dic2:
                dic2[s] = 1
            else:
                dic2[s] += 1
        ans = []
        for key in dic1:
            if dic1[key] == 1 and key not in dic2:
                ans.append(key)
        for key in dic2:
            if dic2[key] == 1 and key not in dic1:
                ans.append(key) 
        return ans
        
                
                