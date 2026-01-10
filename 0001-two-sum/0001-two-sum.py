class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        da_gap = {}
        for j in range(len(nums)):
            start = nums[j]
            so_can_tim = target - start
            if so_can_tim in da_gap:
                return [da_gap[so_can_tim], j]
            da_gap[start] = j
        return []

