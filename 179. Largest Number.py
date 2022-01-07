def largestNumber(nums):
    """
    :type nums: List[int]
    :rtype: str
    """
    for i in range(len(nums)):
        nums[i] = str(nums[i])
    
    nums.sort()
    print(nums)
    for j in range(len(nums)-1, 0, -1):
        if nums[j]+nums[j-1] < nums[j-1]+nums[j]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
    print(nums)
    ans = "".join(nums[::-1])
    return ans

nums = [74,21,33,51,77,51,90,60,5,56]
print(largestNumber(nums))
