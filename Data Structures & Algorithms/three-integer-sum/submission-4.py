class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        prev = None
        for i in range(len(nums)):
            if prev is not None and nums[i] == prev:
                continue
            prev = nums[i]
            compliment = self.two_sum(nums, i)
            if compliment:
                for couple in compliment:
                    ans.append([nums[i]]+couple)

        return ans
        

    def two_sum(self, nums_sorted:List[int], target_idx) -> List[List[int]]:
        i = target_idx+1
        j = len(nums_sorted) - 1

        ans = []
        target = -nums_sorted[target_idx]

        while i < j:
            curr = nums_sorted[i] + nums_sorted[j]
            if curr == target:
                ans.append([nums_sorted[i],nums_sorted[j]])
                curr_idx = i
                i += 1
                j -= 1
                while nums_sorted[i] == nums_sorted[curr_idx] and i<j:
                    i+=1
            elif curr < target:
                i += 1
            else:
                j -= 1

        print(ans)
        return ans