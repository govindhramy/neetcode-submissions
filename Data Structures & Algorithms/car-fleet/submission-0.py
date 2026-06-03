class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0

        curr_t = 0
        for pos, spd in sorted(zip(position,speed),reverse=True):
            arrival_time = (target-pos)/spd
            if curr_t==0 or arrival_time > curr_t:
                curr_t = arrival_time
                res+=1
        
        return res


