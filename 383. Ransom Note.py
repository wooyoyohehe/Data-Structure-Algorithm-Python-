class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote)>len(magazine):
            return False
        dic = {}
        for m in magazine:
            if m not in dic:
                dic[m] = 1
            else:
                dic[m] += 1
        for r in ransomNote:
            if r not in dic:
                return False
            elif dic[r] <= 0:
                return False
            else:
                dic[r] -= 1
        return True