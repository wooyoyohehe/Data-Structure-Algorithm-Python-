# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):
            
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.push_left(root)
        
    def push_left(self, p):
        while p:
            self.stack.append(p)
            p = p.left
    
    def next(self):
        """
        :rtype: int
        """
        cur = self.stack.pop()
        self.push_left(cur.right)
        return cur.val
        
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack:
            return True
        else:
            return False
            
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()