class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 1:
            return 'A'<= word[0]<= 'Z' or 'a'<= word[0]<= 'z'
        if 'a'<= word[0]<= 'z':
            for i in range(1, len(word)):
                if word[i] < 'a' or word[i] > 'z':
                    return False
        if 'A'<= word[0]<= 'Z':
            if 'A'<= word[1]<= 'Z':
                for i in range(2, len(word)):
                    if word[i] < 'A' or word[i] > 'Z':
                        return False
            if 'a'<= word[1]<= 'z':
                for i in range(2, len(word)):
                    if word[i] < 'a' or word[i] > 'z':
                        return False
        return Trueclass Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 1:
            return 'A'<= word[0]<= 'Z' or 'a'<= word[0]<= 'z'
        if 'a'<= word[0]<= 'z':
            for i in range(1, len(word)):
                if word[i] < 'a' or word[i] > 'z':
                    return False
        if 'A'<= word[0]<= 'Z':
            if 'A'<= word[1]<= 'Z':
                for i in range(2, len(word)):
                    if word[i] < 'A' or word[i] > 'Z':
                        return False
            if 'a'<= word[1]<= 'z':
                for i in range(2, len(word)):
                    if word[i] < 'a' or word[i] > 'z':
                        return False
        return Trueclass Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 1:
            return 'A'<= word[0]<= 'Z' or 'a'<= word[0]<= 'z'
        if 'a'<= word[0]<= 'z':
            for i in range(1, len(word)):
                if word[i] < 'a' or word[i] > 'z':
                    return False
        if 'A'<= word[0]<= 'Z':
            if 'A'<= word[1]<= 'Z':
                for i in range(2, len(word)):
                    if word[i] < 'A' or word[i] > 'Z':
                        return False
            if 'a'<= word[1]<= 'z':
                for i in range(2, len(word)):
                    if word[i] < 'a' or word[i] > 'z':
                        return False
        return True