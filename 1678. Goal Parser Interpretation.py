class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        ans = ""
        i = 0
        while i < len(command):
            if command[i] not in "()":
                ans += command[i]
            elif command[i] == "(" and command[i+1] == ")":
                ans += "o"
                i += 1
            i += 1
        return ans
                