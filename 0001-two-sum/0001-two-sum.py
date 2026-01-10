class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        sum = None
        while sum!=target and i < len(nums) - 1:
            for k in range(0,j-i):
                sum = nums[i] + nums[j]
                if sum != target:
                    j-=1
                elif sum == target:
                    return[i, j]
            i+=1
            j = len(nums) - 1
        return []

