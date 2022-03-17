class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack = []
        ans = [0]*n
        for log in logs:
            log = log.split(":")
            if log[1] == "start":
                stack.append(log)
            else:
                time = int(log[2])-int(stack.pop()[2])+1
                ans[int(log[0])] += time
                if stack:
                    ans[int(stack[-1][0])] -= time
        return ans


