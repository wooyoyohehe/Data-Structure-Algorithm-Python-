class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        letters = []
        ans = []
        for ss in s:
            if "a"<=ss<="z" or "A"<=ss<="Z":
                letters.append(ss)
            ans.append(ss)
        i = len(letters)-1
        for j in range(len(ans)):
            if "a"<=ans[j]<="z" or "A"<=ans[j]<="Z":
                ans[j] = letters[i]
                i -= 1
        return "".join(ans)
        