class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        p = 0
        q = 0
        dic = {}
        count = 0
        ans = ""
        while q < len(paragraph):
            while q < len(paragraph) and paragraph[q] not in "!?',;. ":
                q += 1
            word = paragraph[p:q].lower()
            if word not in banned:
                if word not in dic:
                    dic[word] = 1
                else:
                    dic[word] += 1
                if dic[word] > count:
                    ans = word
                    count = dic[word]
            while q < len(paragraph) and paragraph[q] in "!?',;. ":
                q += 1
            p = q
        return ans
                    
                    
        
        
                