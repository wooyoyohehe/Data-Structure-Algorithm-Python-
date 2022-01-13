nums = [1,2,1,1,1]
step = 0
cur = 0
if nums[0] >= len(nums)-1:
    print(1)
    exit(0)
while 1:
    max_jump = -1
    max_index = -1
    for i in range(cur+1, cur+nums[cur]+1):
        if nums[i] >= max_jump:
            max_index = i
            max_jump = nums[i]
    print(cur)
    cur = max_index
    step += 1
    if cur + nums[cur] >= len(nums)-1:
        step += 1
        print(step)
        exit(0)