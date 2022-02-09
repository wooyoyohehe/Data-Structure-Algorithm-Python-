class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        if n <= 2:
            return True
        dic = dict()
        for edge in edges:
            if edge[0] not in dic:
                dic[edge[0]] = [edge[1]]
            else:
                dic[edge[0]].append(edge[1])
            if edge[1] not in dic:
                dic[edge[1]] = [edge[0]]
            else:
                dic[edge[1]].append(edge[0])
        q = [source]
        visited = set()
        while q:
            cur = q.pop(0)
            for node in dic[cur]:
                if node == destination:
                    return True
                if node in visited:
                    continue
                visited.add(node)
                q.append(node)
        return False