class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        def collision(cur):
            while stack and stack[-1]>0 and cur<0:
                if stack[-1] == -cur:
                    stack.pop()
                    return
                elif stack[-1] < -cur:
                    stack.pop()
                else:
                    return
            stack.append(cur)
            return
                
        stack = []
        for i in range(len(asteroids)):
            if not stack or not (stack[-1]>0 and asteroids[i]<0):
                stack.append(asteroids[i])
            else:   
                collision(asteroids[i])
        return stack
                        
                        
                        
                    
            
        