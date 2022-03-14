class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adj = {}
        nodes = set()
        for edge in edges:
            if edge[0] not in adj:   
                adj[edge[0]] = set()
            adj[edge[0]].add(edge[1])
            if edge[1] not in adj:   
                adj[edge[1]] = set()
            adj[edge[1]].add(edge[0])
            nodes.add(edge[0])
            nodes.add(edge[1])
        count = 0
        num = len(nodes)
        while nodes:
            q = [nodes.pop()]
            visited = set()
            while q:
                cur = q.pop(0)
                visited.add(cur)
                for node in adj[cur]:
                    if node not in visited:
                        q.append(node)
                        visited.add(node)
            nodes -= visited
            count += 1
        return count+n-num
            
        