# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = deque([[root, 1]])
        ans = 1
        while q:
            for _ in range(len(q)):
                cur, num = q.popleft()
                if cur.left:
                    q.append([cur.left, num*2])
                if cur.right:
                    q.append([cur.right, num*2+1])
            if len(q) >= 2:
                ans = max(ans, q[-1][1] - q[0][1]+1)
        return ans
            
            
        
            
        