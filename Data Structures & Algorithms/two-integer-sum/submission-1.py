class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, fn in enumerate(nums):
            sn = target - fn
            if sn in seen:
                return [seen[sn], i]
            seen[fn] = i
