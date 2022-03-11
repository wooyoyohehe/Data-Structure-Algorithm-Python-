class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dic = {}
        for i in range(len(codes)):
            dic[i] = codes[i]
        trans = set()
        for word in words:
            temp = ""
            for letter in word:
                temp += dic[ord(letter)-ord("a")]
            trans.add(temp)
        return len(trans)
            
            
        