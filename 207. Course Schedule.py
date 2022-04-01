class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        edges = {}
        in_degree = [0]*numCourses
        for p in prerequisites:
            if p[0] not in edges:
                edges[p[0]] = []
            edges[p[0]].append(p[1])
            in_degree[p[1]] += 1
        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        visited = 0
        while q:
            v = q.popleft()
            visited += 1
            if v in edges:
                for course in edges[v]:
                    in_degree[course] -= 1
                    if in_degree[course] == 0:
                        q.append(course)
        return visited == numCourses