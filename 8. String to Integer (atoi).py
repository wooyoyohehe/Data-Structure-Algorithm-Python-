class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        flag = 1
        i=0
        result = 0
        while 1:
            if s[i] == ' ':
                if i == len(s)-1:
                    return 0
                else:
                    i+=1
                    continue
            if s[i] == '.' or 'A' <= s[i] <= 'Z' or 'a' <= s[i] <= 'z':
                return 0
            if s[i] == '+' or s[i] == '-':
                if i == len(s)-1:
                    return 0
                if s[i+1]<'0' or s[i+1]>'9':
                    return 0
                break
            if '0' <= s[i] <= '9':
                break
        if s[i] == '+' or s[i] == '-':
            if s[i] == '-':
                flag = 0
            i+=1
        while i<len(s) and'0'<=s[i]<='9':
            result = 10*result+int(s[i])
            i+=1
        if flag == 0:
            result = -result
            if result<-2**31:
                return -2**31   
        if result > 2**31-1:
            return 2**31-1
        return result