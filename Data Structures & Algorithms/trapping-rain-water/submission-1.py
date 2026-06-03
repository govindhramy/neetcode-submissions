class Solution:
    def trap(self, height: List[int]) -> int:
        
        prefix_max = [0]*len(height)
        suffix_max = [0]*len(height)

        m = None
        for i in range(len(height)):
            if m is not None and height[m] > height[i]:
                prefix_max[i] = m
            else:
                prefix_max[i] = None
                m = i

        m = None
        for i in range(len(height)-1,-1,-1):
            if m is not None and height[m] > height[i]:
                suffix_max[i] = m
            else:
                suffix_max[i] = None
                m = i
        
        ans = 0
        for i, h in enumerate(height):
            p = prefix_max[i]
            s = suffix_max[i]
            if p is None or s is None:
                continue
            ans += (min(height[p],height[s]) - h)
        return ans