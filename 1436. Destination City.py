class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        start = set()
        for path in paths:
            start.add(path[0])
        for path in paths:
            if path[1] not in start:
                return path[1]
            