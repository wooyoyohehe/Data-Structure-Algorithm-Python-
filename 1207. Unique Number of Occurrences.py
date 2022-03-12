class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dic = {}
        for num in arr:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        occr = set()
        for key in dic:
            occr.add(dic[key])
        return len(occr) == len(dic)