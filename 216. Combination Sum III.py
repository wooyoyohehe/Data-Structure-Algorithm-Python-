class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        nums = [0,1,2,3,4,5,6,7,8,9]
        def helper(index, path):
            if len(path) == k:
                if sum(path) == n:
                    ans.append(path)
                return
            if sum(path) > n:
                return
            for i in range(index, 10):
                if i >= n:
                    continue
                helper(i+1, path+[i])
        helper(1,[])
        return ans