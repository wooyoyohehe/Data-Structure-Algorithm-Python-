class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        def helper(index, path, ans):
            if len(path) == k:
                ans.append(path)
                return
            for i in range(index+1, n):
                helper(i, path+[i+1], ans)
        helper(-1,[], ans)
        return ans