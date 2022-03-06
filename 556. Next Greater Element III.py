class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = []
        for s in str(n):
            arr.append(ord(s) - ord('0'))
        for i in range(len(arr)-1, 0, -1):
            if arr[i] > arr[i-1]:
                digit = 10
                index = 0
                for k in range(i, len(arr)):
                    if arr[k] > arr[i-1] and arr[k] <= digit:
                        digit = arr[k]
                        index = k 
                arr[index], arr[i-1] = arr[i-1], arr[index]
                left = i
                right = len(arr) - 1
                while left < right:
                    arr[left], arr[right] = arr[right], arr[left]
                    left += 1
                    right -= 1
                ans = 0
                t = 1
                for j in range(len(arr)-1, -1, -1):
                    ans += arr[j] * t
                    t *= 10
                if ans > 2**31-1:
                    return -1
                return ans
        return -1
                
        
        