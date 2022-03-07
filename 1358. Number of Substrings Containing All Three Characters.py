class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {"a":0, "b":0, "c":0}
        left, right,count, ans = 0, 0, 0, 0
        while right < len(s):
            if s[right] in dic:
                if dic[s[right]] == 0:
                    count += 1
                dic[s[right]] += 1
                while count == 3:
                    ans += len(s) - right
                    dic[s[left]] -= 1
                    if dic[s[left]] == 0:
                        count -= 1
                    left += 1
            right += 1
        return ans
                