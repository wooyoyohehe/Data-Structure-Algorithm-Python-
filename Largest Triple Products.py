import math
# Add any extra import statements you may need here
import heapq

# Add any helper functions you may need here


def findMaxProduct(arr):
  # Write your code here
  q = []
  output = [0]*len(arr)
  for i in range(len(arr)):
    if i < 2:
      output[i] = -1
      heapq.heappush(q,arr[i])
    elif i == 2:
      output[i] = arr[0]*arr[1]*arr[2]
      heapq.heappush(q,arr[i])
    else:
      temp = heapq.heappop(q)
      if temp < arr[i]:
        heapq.heappush(q,arr[i])
        output[i] = output[i-1]/temp*arr[i]
      else:
        heapq.heappush(q,temp)
        output[i] = output[i-1]
  return output