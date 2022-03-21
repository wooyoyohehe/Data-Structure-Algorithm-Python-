"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        visited = {}
        q = deque([node])
        visited[node] = Node(node.val, [])
        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei not in visited:
                    q.append(nei)
                    visited[nei] = Node(nei.val, [])
                visited[cur].neighbors.append(visited[nei])
        return visited[node]
        
                    
                    
        