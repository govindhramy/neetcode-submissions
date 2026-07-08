class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        smol, large = (nums2, nums1) if len(nums2) < len(nums1) else (nums1, nums2)
        
        if len(smol) == 0:
            l = len(large)
            if l % 2 == 0:
                return (large[l//2-1] + large[l//2])/2
            else:
                return large[l//2]

        i, j = 0, len(smol)-1

        half = (len(smol)+len(large))//2

        while True:
            mid = (i+j)//2
            large_partition = half - (mid+1)

            smol_left = smol[mid] if mid >=0 else float("-inf")
            smol_right = smol[mid+1] if mid+1 < len(smol) else float("inf")

            large_left = large[large_partition-1] if large_partition-1 >= 0 else float("-inf")
            large_right = large[large_partition] if large_partition < len(large) else float("inf")

            if smol_left <= large_right and large_left <= smol_right:
                if half%2 != 0:
                    return min(smol_right, large_right)
                else:
                    return (max(smol_left, large_left) + min(smol_right, large_right))/2
            
            if smol_left > large_right:
                j = mid-1
            else:
                i = mid+1

