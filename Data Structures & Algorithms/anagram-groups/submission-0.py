class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            m = self.memoize(s)
            if m in d:
                d[m].append(s)
            else:
                d[m] = [s]
        return list(d.values())
        
    def memoize(self, s:str) -> Tuple:
        ans = [0]*26
        for ch in s:
            ans[ord(ch)-ord('a')] += 1
        return tuple(ans)