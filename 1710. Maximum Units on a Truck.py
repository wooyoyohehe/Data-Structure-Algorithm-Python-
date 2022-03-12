class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        q = []
        for box in boxTypes:
            heapq.heappush(q, (-box[1], box[0]))
        box_num = 0
        ans = 0
        while box_num < truckSize and q:
            box = heapq.heappop(q)
            if box_num + box[1] >= truckSize:
                ans += (truckSize-box_num)*(-box[0])
                return ans
            else:
                box_num += box[1]
                ans += (-box[0])*box[1]
        return ans
        