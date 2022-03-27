class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        # [4,-2,1,3]
        # [4,2,1,3]
        # index = val + index_diff
        min_ele = min(arr)
        max_ele = max(arr)
        index_diff = -min_ele
        bucket = [0]*(max_ele-min_ele+1)
        ans = []
        for ele in arr:
            bucket[ele+index_diff] = 1
        min_abs = max_ele-min_ele
        prev = 0
        # [3,8,-10,23,19,-4,-14,27]
        for i in range(1, len(bucket)):
            if bucket[i] == 0:
                continue
            if i - prev < min_abs:
                min_abs = i - prev
                ans = [[prev-index_diff, i-index_diff]]
            elif i - prev == min_abs:
                ans.append([prev-index_diff, i-index_diff])
            prev = i
        return ans
                  
                
        