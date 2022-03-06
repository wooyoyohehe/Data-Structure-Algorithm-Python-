class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        dic = {}
        s = licensePlate.lower()
        for i in range(len(s)):
            if s[i] != " " and not '0' <= s[i] <= '9':
                if s[i] not in dic:
                    dic[s[i]] = 1
                else:
                    dic[s[i]] += 1
        shortest = 16
        index = -1
        for i in range(len(words)):
            temp = dic.copy()
            for letter in words[i]:
                if letter in temp:
                    temp[letter] -= 1
                    if temp[letter] <= 0:
                        temp.pop(letter)
            if not temp and len(words[i]) < shortest:
                shortest = len(words[i])
                index = i      
        return words[index]
                    