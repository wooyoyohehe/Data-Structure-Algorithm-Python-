class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        ans = "11"
        temp = ""
        for j in range(n-2):
            count = 1
            temp = ""
            i = 0
            while 1:
                if i < len(ans)-1 and ans[i] == ans[i+1]:
                    count+=1
                    if i == len(ans)-2:
                        temp+=(str(count)+str(ans[i]))
                        break
                    i+=1
                    continue
                else:
                    temp+=(str(count)+str(ans[i]))
                    i+=1
                    if i == len(ans):
                        break
                    count = 1
            ans = temp
        return ans