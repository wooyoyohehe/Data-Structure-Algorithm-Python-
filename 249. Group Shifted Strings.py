class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        ans = []
        for s in strings:
            if len(s) == 1:
                if len(ans) == 0:
                    ans.append([s])
                else:
                    ans[0].append(s)
            else:
                diff = ""
                for i in range(len(s)-1):
                    if ord(s[i+1]) - ord(s[i]) < 0:
                        diff += str(ord(s[i+1]) - ord(s[i])+26) + ","
                    else:
                        diff += str(ord(s[i+1]) - ord(s[i])) + ","
                if diff not in dic:
                    dic[diff] = [s]
                else:
                    dic[diff].append(s)
        for key in dic:
            ans.append(dic[key])
        return ans