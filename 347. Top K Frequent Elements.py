from queue import PriorityQueue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        q = PriorityQueue()
        for key in dic:
            if q.qsize() == k:
                temp = q.get()
                if temp[0] < dic[key]:
                    q.put([dic[key], key])  
                else:
                    q.put(temp)                  
            else:
                q.put([dic[key], key])
        ans = []
        while not q.empty():
            ans.append(q.get()[1])
        return ans