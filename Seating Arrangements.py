import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def minOverallAwkwardness(arr):
  # Write your code here
  arr.sort()
  i = len(arr)-2
  seats = [arr[-1]]
  cur_left = arr[-1]
  cur_right = arr[-1]
  ans = -1
  while i >= 0:
    ans = max(ans, abs(arr[i]-cur_right))
    cur_right = arr[i]
    i -= 1
    if i >= 0:
      ans = max(ans, abs(arr[i]-cur_left))
      cur_left = arr[i]
  return max(ans, abs(cur_left-cur_right))