class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        j = max(piles)

        while i < j:
            k = (i+j)//2

            hrs = sum([-(pile//-k) for pile in piles])
            if hrs <= h:
                j = k
            else:
                hrs_nxt = sum([-(pile//-(k+1)) for pile in piles])
                if hrs_nxt <=h:
                    return k+1
                i = k
        return j