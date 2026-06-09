class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        res = 0
        j = -1

        for i,ch in enumerate(s):
            if ch in last_seen:
                j = max(last_seen[ch], j)
            last_seen[ch] = i
            res = max(res, i-j)
        return res