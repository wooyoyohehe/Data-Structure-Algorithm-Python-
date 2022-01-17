class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator*denominator<0:
            flag = -1
            numerator = abs(numerator)
            denominator = abs(denominator)
        else:
            flag = 1
        int_part = (numerator//denominator)*flag
        residue = numerator%denominator
        if residue == 0:
            return str(int_part)
        used_residue = [residue]
        cur_res = ""
        ans=""
        while 1:
            residue *= 10
            cur_res = residue // denominator
            residue = residue % denominator
            if residue in used_residue:
                length = len(used_residue) - used_residue.index(residue)
                ans += str(cur_res)
                ans = ans[:len(ans)-length] + "("+ans[-length:]+")"
                break
            elif residue == 0:
                length = len(used_residue)
                ans += str(cur_res)
                break
            else:
                used_residue.append(residue)
                ans += str(cur_res)
        if int_part == 0 and flag == -1:
            return "-" + str(int_part) + "." + ans
        return str(int_part) + "." + ans