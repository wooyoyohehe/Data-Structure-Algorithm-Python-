class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        window = dict()
        target = dict()
        for i in range(len(t)):
            if t[i] not in target:
                target[t[i]] = 1
                window[t[i]] = 0
            else:
                target[t[i]] += 1
        left, right, count, ans = 0, 0, 0, ""
        min_len = float("inf")
        while right < len(s):
            if s[right] in window:
                window[s[right]] += 1
                if window[s[right]] == target[s[right]]:
                    count += 1
                    if count == len(target):
                        while 1:
                            if s[left] in window:
                                if right-left+1 < min_len:
                                    min_len = right-left+1
                                    ans = s[left:right+1]
                                window[s[left]] -= 1
                                if window[s[left]] < target[s[left]]:
                                    left += 1
                                    break
                            left += 1
                        count -= 1
            right += 1
        return ans