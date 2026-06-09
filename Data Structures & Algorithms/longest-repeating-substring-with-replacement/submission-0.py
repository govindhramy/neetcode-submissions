class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # AAAAAABBCCCCCCB
        counts = [0]*26
        tokens = 0
        j=0
        res = 0

        for i,ch in enumerate(s):
            if counts[ord(ch) - ord('A')] < max(counts):
                tokens += 1
            counts[ord(ch) - ord('A')] += 1
            
            while tokens > k:
                counts[ord(s[j]) - ord('A')] -= 1
                if counts[ord(s[j]) - ord('A')] < max(counts):
                    tokens-=1
                j+=1

            res = max(res,i-j+1)

        return res

# 