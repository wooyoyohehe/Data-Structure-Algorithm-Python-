class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        edges = {}
        in_degree = [0]*numCourses
        for p in prerequisites:
            if p[1] not in edges:
                edges[p[1]] = []
            edges[p[1]].append(p[0])
            in_degree[p[0]] += 1
        q = deque()
        ans = []
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                q.append(i)
                ans.append(i)
        while q:
            v = q.popleft()
            if v in edges:
                for node in edges[v]:
                    in_degree[node] -= 1
                    if not in_degree[node]:
                        q.append(node)
                        ans.append(node)
        if len(ans) == numCourses:
            return ans
        else:
            return []
                        
            
                
            