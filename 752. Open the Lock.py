class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        if "0000" in deadends:
            return -1
        if "0000" == target:
            return 0
        visited = set()
        visited.add("0000")
        queue = [("0000",0)]
        direction = [(0,0,0,1), (0,0,0,-1), (0,0,1,0), (0,0,-1,0),(0,1,0,0), (0,-1,0,0), (1,0,0,0), (-1,0,0,0)]
        while len(queue) > 0:
            password, turns = queue.pop(0)
            if password == target:
                return turns
            if password in deadends:
                continue
            for d in direction:
                new_psw = ""
                for i in range(4):
                    if d[i] == 0:
                        new_psw += password[i]
                    else:
                        new_psw += str((int(password[i])+d[i]+10)%10)
                if new_psw in visited:
                    continue
                queue.append((new_psw,turns+1))
                visited.add(new_psw)
        return -1