class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        adj = {}
        cities = set()
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    if i+1 not in adj:
                        adj[i+1] = []
                    adj[i+1].append(j+1)
                    if j+1 not in adj:
                        adj[j+1] = []
                    adj[j+1].append(i+1)
                    cities.add(i+1)
                    cities.add(j+1)
        count = 0
        num = n - len(cities)
        while cities:
            q = [cities.pop()]
            visited = set()
            while q:
                cur = q.pop(0)
                visited.add(cur)
                for city in adj[cur]:
                    if city not in visited:
                        visited.add(city)
                        q.append(city)
            count += 1
            cities -= visited
        return count+num
                    
                
        
                