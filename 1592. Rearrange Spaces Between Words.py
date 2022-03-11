class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        count = 0
        p = 0
        q = 0
        words = []
        while q < len(text):
            while q < len(text) and text[q] == " ":
                count += 1
                q += 1
            p = q
            while q < len(text) and text[q] != " ":
                q += 1
            words.append(text[p:q])
            p = q
        if words[-1] == "":
            words = words[:-1]
        if len(words) == 1:
            return words[0] + " "*count
        interval = count // (len(words)-1)
        extra = count % (len(words)-1)
        ans = ""
        for i in range(len(words)-1):
            ans += words[i]
            ans += interval* " "
        ans += words[-1]
        ans += extra*" "
        return ans
        
        