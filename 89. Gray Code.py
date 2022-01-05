class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 1:
            return [0,1]
        if n == 2:
            return [0,1,3,2]
        temp = ["00", "01", "11", "10"]
        for i in range(n-2):
            ans = []
            for t in temp:
                ans.append("0"+t)
            for i in range(len(temp)-1, -1, -1):
                ans.append("1"+temp[i])
            temp = ans
        for i in range(len(ans)):
            ans[i] = int(ans[i], 2)
        return ans