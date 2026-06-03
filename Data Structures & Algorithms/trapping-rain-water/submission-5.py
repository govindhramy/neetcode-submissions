class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        for i,h in enumerate(height):

            base_h = None
            while stack and stack[-1][1] <= h:
                j,h2 = stack.pop()
                if base_h is None:
                    base_h = h2
                    continue
                ans += (i-j-1)*(h2-base_h)
                base_h = h2
            if stack and base_h is not None:
                ans += (i-stack[-1][0]-1)*(h-base_h)
            stack.append((i,h))

        return ans