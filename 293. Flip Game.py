class Solution(object):
    def generatePossibleNextMoves(self, currentState):
        """
        :type currentState: str
        :rtype: List[str]
        """
        if len(currentState) < 2:
            return []
        ans = []
        for i in range(len(currentState)-1):
            if currentState[i] == currentState[i+1] == "+":
                ans.append(currentState[:i]+"--"+currentState[i+2:])
        return ans