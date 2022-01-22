class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        left = right = 0
        ans = []
        if nums == []:
            return ans
        while right < len(nums)-1:
            if nums[right+1] - nums[right] == 1:
                right += 1
            else:
                if left == right:
                    ans.append(str(nums[left]))
                else:
                    ans.append(str(nums[left])+"->"+str(nums[right]))
                right += 1
                left = right
        if left == right:
            ans.append(str(nums[left]))
        else:
            ans.append(str(nums[left])+"->"+str(nums[right]))
        return ans
            