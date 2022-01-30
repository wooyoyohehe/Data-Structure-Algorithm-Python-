import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = ""
        unused = [i for i in range(n+1)]
        for i in range(n):
            index = math.ceil(k/math.factorial(n-i-1))
            ans += str(unused[index])
            unused.pop(index)
            k -= (index-1) * math.factorial(n-i-1)
        return ans