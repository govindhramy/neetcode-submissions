class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left_dist, right_dist = [], []

        stack = []
        i=0
        while i < len(heights):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left_dist.append(i - stack[-1] - 1)
            else:
                left_dist.append(i)
            stack.append(i)
            i+=1
        
        stack = []
        i=len(heights)-1
        while i >= 0:
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right_dist.append(stack[-1] - i - 1)
            else:
                right_dist.append(len(heights)-1 - i)
            stack.append(i)
            i-=1
        right_dist.reverse()

        ans = 0

        for i,h in enumerate(heights):
            ans = max(ans, h * (1+left_dist[i]+right_dist[i]))
        
        return ans
        