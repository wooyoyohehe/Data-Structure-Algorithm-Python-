# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        q = deque()
        q.append([root, (0,0)])
        dic = {}
        left = 0
        right = 0
        nodes = []
        while q:
            node, [row, col] = q.popleft()
            left = min(left, col)
            right = max(right, col)
            nodes.append((col, row, node.val))
            if node.left:
                q.append([node.left, (row+1, col-1)])
            if node.right:
                q.append([node.right, (row+1, col+1)])
        nodes.sort()
        j = 0     
        for i in range(left, right+1):
            cur_col = []
            while j < len(nodes) and nodes[j][0] == i:
                cur_col.append(nodes[j][2])
                j += 1
            ans.append(cur_col)
        return ans
        
        
                
        