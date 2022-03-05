class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if len(nums) == 0:
            if lower == upper:
                return [str(lower)]
            else:
                return [str(lower) + "->" + str(upper)]
        ans = []
        nums = [lower] + nums + [upper]
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            if nums[i] + 1 == nums[i+1]:
                if i == 0:
                    ans.append(str(lower))
                elif i == len(nums) - 2:
                    ans.append(str(upper))
                else:
                    continue
            elif nums[i] + 2 == nums[i+1]:
                if i == 0:
                    ans.append(str(nums[i]) + "->" + str(nums[i]+1))
                elif i == len(nums) - 2:
                    ans.append(str(nums[i]+1) + "->" + str(nums[i+1]))
                else:
                    ans.append(str(nums[i]+1))
            else:
                if i == len(nums)-2:
                    ans.append(str(nums[i]+1) + "->" + str(nums[i+1]))
                else:
                    if i == 0:
                        ans.append(str(nums[i]) + "->" + str(nums[i+1]-1))
                    else:
                        ans.append(str(nums[i]+1) + "->" + str(nums[i+1]-1))
        return ans
        