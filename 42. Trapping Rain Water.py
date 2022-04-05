class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #                        v
        # [0,1,0,2,1,0,1,3,2,1,2,1]
        #    ^       
        # lmax = 0
        # rmax = 1
        # ans = 0
        left = 0
        right = len(height)-1
        lmax = height[0]
        rmax = height[-1]
        ans = 0
        while left < right:
            if lmax <= rmax:
                ans += lmax-height[left]
                left += 1
                lmax = max(lmax, height[left])
            else:
                ans += rmax-height[right]
                right -= 1
                rmax = max(rmax,height[right])
        return ans
            
        
        # l_max = [0]*len(height)
        # r_max = [0]*len(height)
        # lmax = 0
        # for i in range(len(height)):
        #     l_max[i] = lmax
        #     lmax = max(height[i], lmax)
        # rmax = 0
        # for i in range(len(height)-1, -1, -1):
        #     r_max[i] = rmax
        #     rmax = max(height[i], rmax)
        # ans = 0
        # for i in range(len(height)):
        #     ans += max(min(l_max[i], r_max[i])-height[i], 0)
        # return ans            