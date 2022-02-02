# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def del_node(root, parent, pos):
            if parent:
                target = root
                if pos == 1:
                    target = parent.left
                if pos == 0:
                    target = parent.right
                if target.right:
                    if not target.right.left:
                        target.right.left = target.left
                        if pos == 1:
                            parent.left = target.right
                        elif pos == 0:
                            parent.right = target.right
                        else:
                            root = root.right
                    else:
                        node = target.right
                        while node.left.left:
                            node = node.left
                        target.val = node.left.val
                        node.left = node.left.right
                elif target.left and not target.right:
                    if pos == 1:
                        parent.left = target.left
                    elif pos == 0:
                        parent.right = target.left
                    else:
                        root = root.left
                else:
                    if pos == 1:
                        parent.left = target.right
                    elif pos == 0:
                        parent.right = target.right
                    else:
                        return None
            return root
 
        parent = root
        while parent:
            if parent.val > key:
                if parent.left and parent.left.val == key:
                    return del_node(root, parent, 1)
                else:
                    parent = parent.left
            elif parent.val < key:
                if parent.right and parent.right.val == key:
                    return del_node(root, parent, 0)
                else:
                    parent = parent.right
            else:
                return del_node(root, root, -1)
        return root