class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        right = 0
        max_ = 0
        while right != len(s):
            temp_array = []
            length = 0
            while s[right] not in temp_array:
                temp_array.append(s[right])
                length += 1
                right += 1
                if right == len(s):
                    return max(max_, length)
            right = right - (len(temp_array)-1)
            max_ = max(max_, length)
        return max_