class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = dict()
        for ss in s:
            if ss not in dic:
                dic[ss] = 1
            else:
                dic[ss] += 1
        unvisited = ""
        count = 0
        for key in dic:
            if dic[key]%2 == 0:
                unvisited += key*(dic[key]/2)
            else:
                if dic[key] != 1:
                    unvisited += key
                mid = key
                count+=1
        if count > 1:
            return []
        length = len(unvisited)
        ans = set()
        def backtrack(string, unvisited):
            if len(string) == length:
                if count == 1:
                    string = string + mid + string[::-1]
                else:
                    string = string + string[::-1]
                ans.add(string)
            for i in range(len(unvisited)):
                backtrack(string + unvisited[i], unvisited[:i] + unvisited[i+1:])
        backtrack("", unvisited)
        return list(ans)