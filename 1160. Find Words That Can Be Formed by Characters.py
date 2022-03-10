class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        dic = {}
        for ch in chars:
            if ch not in dic:
                dic[ch] = 1
            else:
                dic[ch] += 1
        ans = 0
        for word in words:
            flag = True
            dic1 = dic.copy()
            for w in word:
                if w not in dic1:
                    flag = False
                    break
                else:
                    dic1[w] -= 1
                    if dic1[w] < 0:
                        flag = False
                        break
            if flag:
                ans += len(word)
        return ans
                    
                