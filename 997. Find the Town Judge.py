class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if n == 1:
            return 1
        people = set()
        list_ = [0]*(n+1)
        for t in trust:
            list_[t[1]] += 1
            people.add(t[0])
        for i in range(1, len(list_)):
            if list_[i] == n-1 and i not in people:
                return i
        return -1
    