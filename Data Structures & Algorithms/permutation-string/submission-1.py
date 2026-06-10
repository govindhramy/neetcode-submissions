import string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = {el:0 for el in string.ascii_lowercase}
        for ch in s1:
            c1[ch] += 1

        c2 = {el:0 for el in string.ascii_lowercase}
        for ch in s2[:len(s1)]:
            c2[ch] += 1
        if c1 == c2:
            return True

        j=1
        for i in range(len(s1), len(s2)):
            c2[s2[j-1]] -= 1
            c2[s2[i]] += 1

            if c2 == c1:
                return True
            j+=1

        return False