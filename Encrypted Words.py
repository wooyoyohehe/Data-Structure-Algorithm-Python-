def findEncryptedWord(s):
  # Write your code here
  ans = [""]
  def helper(s):
    if s == "":
        return 
    mid = (len(s)-1)//2
    ans[0] += s[mid]
    helper(s[:mid])
    helper(s[mid+1:])
  helper(s)
  return ans[0]

print(findEncryptedWord("facebook"))