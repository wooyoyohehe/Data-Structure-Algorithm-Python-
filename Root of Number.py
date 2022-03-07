def root(x, n):
  left = 0
  right = x
  while left < right:
    mid = left+(right-left)/2.0
    print(mid)
    if abs(mid ** n - x) < 0.001:
      return mid
    if mid ** n > x:
      rigth = mid
    else:
      left = mid
  return x
print(root(7,3))      