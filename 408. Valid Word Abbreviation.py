class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i = 0
        j = 0
        while i < len(abbr) and j < len(word):
            if abbr[i] == "0":
                return False
            elif "a" <= abbr[i] <= "z":
                if word[j] != abbr[i]:
                    return False
                else:
                    i+=1
                    j+=1
            else:
                num = ""
                while i < len(abbr) and "0"<= abbr[i] <= "9":
                    num += abbr[i]
                    i += 1
                j += int(num)
        return i == len(abbr) and j == len(word)
            
                
                    
                
        