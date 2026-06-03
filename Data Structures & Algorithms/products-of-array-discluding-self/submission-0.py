from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        zero_count = 0
        nz_prod = 1

        for n in nums:
            if n == 0:
                zero_count += 1
            else:
                nz_prod *= n
        
        if zero_count > 1:
            return [0]*len(nums)
        elif zero_count == 1:
            return [nz_prod if n == 0 else 0 for n in nums]
        else:
            return [nz_prod//n for n in nums]