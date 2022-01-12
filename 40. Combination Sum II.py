class Solution(object):
    def combinationSum2(self,candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if sum(candidates) < target:
            return []
        if sum(candidates) == target:
            return [candidates]
        def helper(index, target, path, result):
            if target < 0:
                return
            if target == 0:
                result.append(path)
                return 
            for i in range(index, len(candidates)):
                if i > index and candidates[i - 1] == candidates[i]:
                    continue
                helper(i+1, target - candidates[i], path+[candidates[i]], result)
        result = []
        candidates.sort()
        helper(0, target, [], result)
        return result