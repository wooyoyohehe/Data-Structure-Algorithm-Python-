

def minCut(s):
    """
    :type s: str
    :rtype: int
    """
    def backtrack(s, path, count):
        print(s)
        if s == s[::-1]:
            path = path + [s]
            ans.append(path)
            print(count)
            return
        for i in range(len(s),1,-1):
            if s[:i] == s[:i][::-1]:
                print(s[:i])
                backtrack(s[i:], path + [s[:i]], count+1)
            else:
                continue
    ans = []
    backtrack(s, [], 0)
    return ans

print(minCut("ababababababababababababcbabababababababababababa"))