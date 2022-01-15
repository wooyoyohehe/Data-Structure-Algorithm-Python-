class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) <= 3:
            return []
        if len(nums) == 4:
            if sum(nums) == target:
                return [nums]
            else:
                return []
            
        nums.sort()
        ans = []
        p1 = 0
        while p1 != len(nums) - 3:
            if p1>0 and nums[p1] == nums[p1-1]:
                p1 += 1
                continue
            for p2 in range(p1+1, len(nums)-2):
                if p2 > p1+1 and nums[p2] == nums[p2-1]:
                    continue
                p3 = p2+1
                p4 = len(nums)-1
                while p3 < p4:
                    if nums[p1]+nums[p2]+nums[p3]+nums[p4] == target:
                        ans.append([nums[p1], nums[p2], nums[p3], nums[p4]])
                        while p3 < p4 and nums[p3] == nums[p3+1]:
                            p3 += 1
                        p3 += 1
                        while p3 < p4 and nums[p4] == nums[p4-1]:
                            p4 -= 1
                        p4 -= 1
                    elif nums[p1]+nums[p2]+nums[p3]+nums[p4] < target:
                        p3 += 1
                    elif nums[p1]+nums[p2]+nums[p3]+nums[p4] > target:
                        p4 -= 1
            p1 += 1
        return ans