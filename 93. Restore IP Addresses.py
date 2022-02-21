class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) > 12 or len(s) < 4:
            return []
        ans = []
        def backtrack(remainder, path, length, seg):
            if seg > 4:
                return
            if length == len(s) and seg == 4:
                ans.append(path[:-1])
            for i in range(1, 4):
                if len(remainder[:i]) == 0:
                    continue
                if remainder[:i][0] == "0" and len(remainder[:i]) > 1:
                    continue
                if 0 <= int(remainder[:i]) <= 255:
                    backtrack(remainder[i:], path+remainder[:i]+".", length+i, seg+1)
        backtrack(s, "", 0, 0)
        return ans