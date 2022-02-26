class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = dict()
        dic["0"] = s.count("z")
        dic["2"] = s.count("w")
        dic["4"] = s.count("u")
        dic["6"] = s.count("x")
        dic["8"] = s.count("g")
        dic["3"] = s.count("h") - dic["8"]
        dic["5"] = s.count("f") - dic["4"]
        dic["7"] = s.count("s") - dic["6"]
        dic["9"] = s.count("i") - dic["5"] - dic["6"] - dic["8"]
        dic["1"] = s.count("n") - dic["7"] - 2*dic["9"]
        ans = ""
        for key in ["0","1","2","3","4","5","6","7","8","9"]:
            if dic[key] > 0:
                ans+=key*dic[key]
        return ans
                
        