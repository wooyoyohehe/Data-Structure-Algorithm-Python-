import heapq
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        dic = {}
        q = []
        for word in words:
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] += 1
        for key, val in dic.items():
            heapq.heappush(q, (-val, key))
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(q)[1])
        return ans