class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            val1 = numbers[left]
            val2 = numbers[right]
            curSum = val1 + val2
            if curSum > target:
                right -= 1
            elif curSum < target:
                left += 1
            else:
                return [left+1,right+1]
