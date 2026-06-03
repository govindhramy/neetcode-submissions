class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        n = str(len(strs))
        l = [str(len(s)) for s in strs]

        metadata = n + "," + ",".join(l) + ","
        data = "".join(strs)

        return metadata + data
        

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        idx = s.find(",")
        n = int(s[:idx])
        lengths = []
        for i in range(n):
            nxt = s.find(",",idx+1)
            lengths.append(int(s[idx+1:nxt]))
            idx = nxt

        data = s[idx+1:]

        res = []
        idx = 0
        for l in lengths:
            res.append(data[idx:idx+l])
            idx += l
        return res

        


