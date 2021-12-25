class Solution(object):
    def longestCommonPrefix(self,strs):
        if len(strs)==1:
            return strs[0]
        else:
            min_len = len(strs[0])
            for j in range(1, len(strs)):
                min_len = min(min_len, len(strs[j]))
            num = 0
            for i in range(min_len):
                temp = strs[0][i]
                for str_ in strs:
                    if str_[i] == temp:
                        continue
                    else:
                        return strs[0][:num]
                num += 1
            return strs[0][:num]
                    
                    
        