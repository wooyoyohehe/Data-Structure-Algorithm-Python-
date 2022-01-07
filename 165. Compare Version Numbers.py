def helper(v1,v2, res):
    for i in range(len(v1)):
        if int(v1[i]) > int(v2[i]):
            return res
        if int(v1[i]) < int(v2[i]):
            return -res
    for hehe in v2[len(v1):]:
        if int(hehe) != 0:
            return -res
    return 0
    
    
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split(".")
        v2 = version2.split(".")
        if len(v1) < len(v2):
            return helper(v1,v2, 1)        
        else:
            return helper(v2,v1, -1)