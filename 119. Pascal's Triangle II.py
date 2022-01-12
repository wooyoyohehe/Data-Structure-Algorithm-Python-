class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        row = [1,1]
        for i in range(rowIndex-1):
            tmp = []
            for j in range(len(row)-1):
                tmp.append(row[j]+row[j+1])
            row = [1]+tmp+[1]
        return row