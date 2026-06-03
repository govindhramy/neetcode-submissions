class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        curr_sum = numbers[left] + numbers[right]

        while left < right:
            if curr_sum == target:
                return [left+1,right+1]
            if curr_sum < target:
                curr_sum = curr_sum - numbers[left]
                left += 1
                curr_sum = curr_sum + numbers[left]
            else:
                curr_sum = curr_sum - numbers[right]
                right -= 1
                curr_sum = curr_sum + numbers[right]
        return None