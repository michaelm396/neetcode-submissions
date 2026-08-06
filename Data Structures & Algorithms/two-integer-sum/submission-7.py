class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1) store difference = target - value dictionary
        # 2) if difference in dictionary, return value in dictionary
        prev = {}

        for i,n in enumerate(nums):
            diff = target -n
            if diff in prev:
                return [prev[diff], i]
            prev[n] = i
        return
                    