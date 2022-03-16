class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 1. num
            # has_num = True
        # 2. dot
            # 1. not alone
            # 2. not after E
            # 3. no twice
            # 4. has_dot = True
        # 3. E or e
            # 1. should has_num 
            # 2. no twice
            # 3. not at the end
            # has_e = True
        # 4. + or -
            # 1. should at the beginning
            # 2. should right after E or e
            # 3. not the last one
        has_num = False
        has_dot = False
        has_e = False
        for i in range(len(s)):
            if "0" <= s[i] <= "9":
                has_num = True
            elif s[i] == ".":
                if len(s) == 1 or has_dot or has_e:
                    return False
                has_dot = True
            elif s[i] in "Ee":
                if has_e:
                    return False
                if not has_num:
                    return False
                if i == len(s)-1:
                    return False
                has_e = True
            elif s[i] in "+-":
                if i != 0 and s[i-1] not in "Ee":
                    return False
                if i == len(s)-1:
                    return False
            else:
                return False
        return has_num

                
                