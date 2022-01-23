def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dp = [[0 for _ in range(2)] for _ in range(len(nums))]
    dp[0][1] = 10
    print(dp)

print(maxProduct([-2,3,-4,5,-6]))