class Solution(object):
    def treeDiameter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        if len(edges) <= 2:
            return len(edges)
        dic = dict()
        for x,y in edges:
            if x not in dic:
                dic[x] = [y]
            else:
                dic[x].append(y)
            if y not in dic:
                dic[y] = [x]
            else:
                dic[y].append(x)
        max_edges = 0
        vertix = -1
        for key in dic:
            if len(dic[key])>max_edges:
                vertix = key
                max_edges = len(dic[key])
        
        def bfs(node):
            level = [node]
            visited = [False]*(len(edges)+1)
            ans = -1
            path = 0
            while level:
                temp_level = []
                for node in level:
                    if visited[node]:
                        continue
                    if len(dic[node]) == 1:
                        ans = max(ans, path+1)
                    visited[node] = True
                    temp_level += dic[node]
                if len(temp_level) == 0:
                    leaf = level[0]
                level = temp_level
                path += 1
            return leaf, ans
        
        leaf = bfs(vertix)[0]
        return bfs(leaf)[1]