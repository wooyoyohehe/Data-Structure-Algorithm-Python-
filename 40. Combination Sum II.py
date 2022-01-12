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
                if path not in result:
                    result.append(path)
                return 
            for i in range(index, len(candidates)):
                if i > index and candidates[index - 1] == candidates[index]:
                    continue
                helper(i+1, target - candidates[i], path+[candidates[i]], result)
        result = []
        candidates.sort()
        helper(0, target, [], result)
        return result