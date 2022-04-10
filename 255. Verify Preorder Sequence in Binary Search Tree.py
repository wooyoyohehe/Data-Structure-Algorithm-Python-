class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        """
        idea: stack
        O(n) and O(n)
        """
        stack = []
        cur_small = 0
        for i in range(len(preorder)):
            if preorder[i] < cur_small:
                return False
            else:
                while stack and preorder[i] > stack[-1]:
                    cur_small = stack.pop()
                stack.append(preorder[i])
        return True
                
        
        