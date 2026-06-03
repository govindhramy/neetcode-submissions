class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        ans = 0
        curr = 0

        while i < j:
            curr = (j-i) * min(heights[i],heights[j])
            ans = max(ans,curr)

            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1

        return ans