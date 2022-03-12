class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        dic = {}
        for index in indices:
            for i in range(n):
                if (index[0], i) not in dic:
                    dic[(index[0], i)] = 1
                else:
                    dic[(index[0], i)] += 1
            for j in range(m):
                if (j, index[1]) not in dic:
                    dic[(j, index[1])] = 1
                else:
                    dic[(j, index[1])] += 1
        ans = 0
        for key in dic:
            if dic[key] % 2 == 1:
                ans += 1
        return ans
        