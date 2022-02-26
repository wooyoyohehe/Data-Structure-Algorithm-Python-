class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        diff = area-1
        ans = [area,1]
        for i in range(1, int(area ** 0.5)+2):
            if area % i == 0 and abs(i-area/i) < diff:
                diff = abs(i-area/i)
                ans = [max(i,area/i), min(i,area/i)]
        return ans