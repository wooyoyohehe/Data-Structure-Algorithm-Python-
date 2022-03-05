class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(img)
        n = len(img[0])
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                temp_sum = 0
                num = 0
                for k in range(i-1, i+2):
                    for l in range(j-1, j+2):
                        if 0 <= k < m and 0 <= l < n:
                            num += 1
                            temp_sum += img[k][l]
                ans[i][j] = temp_sum // num
        return ans
        