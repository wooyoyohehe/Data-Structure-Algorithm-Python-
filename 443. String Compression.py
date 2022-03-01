class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        def number2digit(num):
            res = ""
            while num // 10 != 0:
                res = str(num%10) + res
                num = num // 10
            return str(num%10) + res
        left,right,pos = 0,1,0
        while right <= len(chars):
            if right == len(chars) or chars[left] != chars[right]:
                chars[pos] = chars[left]
                pos += 1
            else:
                while right < len(chars) and chars[left] == chars[right]:
                    right += 1
                chars[pos] = chars[left]
                pos += 1
                for dig in number2digit(right-left):
                    chars[pos] = dig
                    pos += 1
            left = right
            right+=1
        return pos