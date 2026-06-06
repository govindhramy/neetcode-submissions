class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r_max = len(matrix) - 1
        c_max = len(matrix[0]) - 1
        if target < matrix[0][0] or target > matrix[r_max][c_max]:
            return False
        
        i = 0
        j = r_max
        r = -1

        while i <= j:
            mid = (i+j)//2
            if mid == r_max or (target >= matrix[mid][0] and target <= matrix[mid][c_max]):
                r = mid
                break
            elif target > matrix[mid][c_max]:
                i = mid+1
            else:
                j = mid-1
        
        if r == -1:
            return False

        i = 0
        j = c_max

        while i <= j:
            mid = (i+j)//2
            if target == matrix[r][mid]:
                return True
            elif target > matrix[r][mid]:
                i = mid+1
            else:
                j = mid-1
        return False