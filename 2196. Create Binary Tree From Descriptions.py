# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        s = set()
        dic = {}
        for des in descriptions:
            s.add(des[1])
            if des[0] not in dic:
                dic[des[0]] = []
            dic[des[0]].append((des[1], des[2]))
        for des in descriptions:
            if des[0] not in s:
                root = TreeNode(des[0])
                q = [root]
                break
        while q:
            node = q.pop(0)
            for child in dic[node.val]:
                child_node = TreeNode(child[0])
                if child[1] == 1:
                    node.left = child_node
                else:
                    node.right = child_node
                if child[0] in dic:
                    q.append(child_node)
        return root