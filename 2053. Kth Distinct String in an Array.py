class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        dic = dict()
        for digit in arr:
            if digit not in dic:
                dic[digit] = 1
            else:
                dic[digit] += 1
        num = 0
        for i in range(len(arr)):
            if dic[arr[i]] == 1:
                num += 1
                if num == k:
                    return arr[i]
        return ""

        