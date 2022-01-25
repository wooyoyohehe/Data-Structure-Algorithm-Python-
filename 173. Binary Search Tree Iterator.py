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
        while root:
            self.stack.append(root)
            root = root.left


    def next(self):
        """
        :rtype: int
        """
        temp = self.stack.pop()
        res = temp.val
        temp = temp.right
        while temp:
            self.stack.append(temp)
            temp = temp.left
        return res


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack != []


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()