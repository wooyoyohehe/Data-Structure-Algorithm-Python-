path = "/home//foo/"
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        path = path.split("/")
        stack =[]
        for p in path:
            if p == "..":
                if stack:
                    stack.pop()
            elif p != "." and p!="":
                stack.append(p)
        return  "/" + "/".join(stack)