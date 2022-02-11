class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        def match(list1,list2):
            for i in range(26):
                if list1[i] != list2[i]:
                    return False
            return True

        if len(s2)<len(s1):
            return False
        list1 = [0]*26
        list2 = [0]*26
        for s in s1:
            list1[ord(s)-ord("a")] += 1
        for s in s2[:len(s1)]:
            list2[ord(s)-ord("a")] += 1
        if match(list1,list2):
            return True
        for i in range(1, len(s2)-len(s1)+1):
            list2[ord(s2[i-1])-ord("a")] -= 1
            list2[ord(s2[i+len(s1)-1])-ord("a")] += 1
            if match(list1,list2):
                return True
        return False