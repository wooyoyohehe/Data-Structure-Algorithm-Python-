class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        m = len(image)
        n = len(image[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        queue = [[sr,sc]]
        oldColor = image[sr][sc]
        image[sr][sc] = newColor
        if oldColor == newColor:
            return image
        while len(queue)>0:
            x,y = queue.pop(0)
            for dx,dy in directions:
                row = x+dx
                col = y+dy
                if not (0<=row<m and 0<=col<n):
                    continue
                if image[row][col] != oldColor:
                    continue
                image[row][col] = newColor
                queue.append([row,col])
        return image