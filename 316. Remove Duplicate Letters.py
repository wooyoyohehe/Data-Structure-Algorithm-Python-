class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        for letter in s:
            if letter not in dic:
                dic[letter] = 1
            else:
                dic[letter] += 1
        stack = []
        for letter in s:
            if letter in stack:
                dic[letter] -= 1
            elif stack and stack[-1] > letter:
                while stack and stack[-1] > letter:
                    if dic[stack[-1]] > 0:
                        stack.pop()
                    else:
                        break
                stack.append(letter)
                dic[letter] -= 1
            else:
                stack.append(letter)
                dic[letter] -= 1
        return "".join(stack)