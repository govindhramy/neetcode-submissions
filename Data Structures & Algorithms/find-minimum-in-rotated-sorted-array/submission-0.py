class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)-1
        ans = float('inf')

        while i <= j:
            mid = (i+j)//2

            if nums[mid] < ans:
                ans = nums[mid]
            if nums[j] < nums[mid]:
                i = mid+1
            else:
                j = mid-1
        return ans
        