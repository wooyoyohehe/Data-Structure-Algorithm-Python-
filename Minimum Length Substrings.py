import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def min_length_substring(s, t):
  # Write your code here
  if len(s) < len(t):
    return -1
  target = dict()
  window = dict()
  for tt in t:
    if tt not in target:
      target[tt] = 1
      window[tt] = 0
    else:
      target[tt] += 1
  left, right, count, ans = 0,0,0,float("inf")
  while right < len(s):
    if s[right] in target:
      window[s[right]] += 1
      if window[s[right]] == target[s[right]]:
        count += 1
        if count == len(target):
          while 1:
            if s[left] in window:
              ans = min(ans, right-left+1)
              window[s[left]] -= 1
              if window[s[left]] < target[s[left]]:
                count -= 1
                left += 1
                break
            else:
              left += 1
    right+=1
  if ans == float("inf"):
    return -1
  return ans





# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  s1 = "dcbefebce"
  t1 = "fd"
  expected_1 = 5
  output_1 = min_length_substring(s1, t1)
  check(expected_1, output_1)

  s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
  t2 = "cbccfafebccdccebdd"
  expected_2 = -1
  output_2 = min_length_substring(s2, t2)
  check(expected_2, output_2)

  # Add your own test cases here
  