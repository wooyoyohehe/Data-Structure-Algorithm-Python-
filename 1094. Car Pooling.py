class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        current = []
        for trip in trips:
            current.append([trip[1], trip[0]])
            current.append([trip[2], -trip[0]])
        current.sort() 
        i = 1
        while i != len(current):
            if current[i][0] == current[i-1][0]:
                current[i-1][1] += current[i][1] 
                current.pop(i)
            else:
                i+=1
        now = 0
        for cur in current:
            now += cur[1]
            if now > capacity:
                return False
        return True 