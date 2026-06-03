class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0

        while s:
            seed = s.pop()
            curr = 1

            left = seed - 1
            right = seed + 1

            while left in s:
                s.remove(left)
                curr += 1
                left -= 1
            
            while right in s:
                s.remove(right)
                curr += 1
                right += 1
            
            ans = max(ans,curr)
        
        return ans