import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        q = []
        for interval in intervals:
            if q and interval[0] >= q[0][0]:
                heapq.heappop(q)
                heapq.heappush(q, (interval[1], interval[0]))
            else:
                heapq.heappush(q, (interval[1], interval[0]))
        return len(q)
        
        