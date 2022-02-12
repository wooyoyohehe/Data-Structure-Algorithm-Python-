
import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def getMilestoneDays(revenues, milestones):
  # Write your code here
  ans = []
  cur_rev = 0
  for i in range(len(revenues)):
    cur_rev += revenues[i]
    revenues[i] = cur_rev
  for j in range(len(milestones)):
    if milestones[j] > revenues[-1]:
      ans.append(-1)
      continue
    left = 0
    right = len(revenues)-1
    while left <= right:
      mid = left + (right-left)//2
      if revenues[mid] >= milestones[j]:
        if revenues[mid-1] < milestones[j]:
          ans.append(mid+1)
          break
        right = mid -1
      else:
        left = mid + 1
      if right == -1:
        ans.append(1)
  return ans
    
    
  
  
  
  
  
  
  
  

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  revenues_1 = [100, 200, 300, 400, 500]
  milestones_1 = [300, 800, 1000, 1400]
  expected_1 = [2, 4, 4, 5]
  output_1 = getMilestoneDays(revenues_1, milestones_1)
  check(expected_1, output_1)

  revenues_2 = [700, 800, 600, 400, 600, 700]
  milestones_2 = [3100, 2200, 800, 2100, 1000] 
  expected_2 = [5, 4, 2, 3, 2]
  output_2 = getMilestoneDays(revenues_2, milestones_2)
  check(expected_2, output_2)

  # Add your own test cases here
  

revenues = [700, 800, 600, 400, 600, 700]
milestones = [3100, 2200, 800, 2100, 1000] 
print(getMilestoneDays(revenues, milestones))