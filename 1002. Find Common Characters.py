class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        check = list(words[0])
        for word in words[1:]:
            new_check = []
            for letter in word:
                if letter in check:
                    new_check.append(letter)
                    check.remove(letter)
            check = new_check
        return check
                    
        