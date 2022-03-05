# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        def helper(string):
            if not string:
                return None
            i, num, sign = 0, 0, 1
            if string[0] == "-":
                i = 1
                sign = -1
            while i < len(string) and string[i] != "(":
                num = num*10 + ord(string[i]) - ord("0")
                i += 1
            root = TreeNode(num*sign)
            if i != len(string):
                start = i
                left_bracket = 1
                while left_bracket:
                    i += 1
                    if string[i] == "(":
                        left_bracket += 1
                    elif string[i] == ")":
                        left_bracket -= 1
                root.left = helper(string[start+1:i])
                root.right = helper(string[i+2:-1])
            return root
        return helper(s)
        
                
        