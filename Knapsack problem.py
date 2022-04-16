capacity = 4
num = 3
weights = [2,1,3]
values = [4,2,3]
dp = [[0 for _ in range(capacity+1)] for _ in range(num+1)]
for i in range(1, len(dp)):
    for j in range(1, len(dp[0])):
        if weights[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]]+values[i-1])
print(dp)
print(dp[-1][-1])
