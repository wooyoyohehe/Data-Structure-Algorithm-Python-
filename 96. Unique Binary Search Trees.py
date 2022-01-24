class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [1,1,2,5]
        i = 4
        while i < n+1:
            temp_ans = 0
            left = 0
            right = i-1
            while left < right:
                temp_ans += 2*ans[left]*ans[right]
                left += 1
                right -= 1
                if left == right:
                    temp_ans += ans[left]*ans[right]
            ans.append(temp_ans)
            i+=1
        return ans[n]