class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        dic = {}
        for item in items:
            if item[0] not in dic:
                dic[item[0]] = [item[1]]
            else:
                dic[item[0]].append(item[1])
        ans = []
        for key in sorted(dic.keys()):
            ans.append([key, sum(sorted(dic[key])[-5:])//5])
        return ans
        
        