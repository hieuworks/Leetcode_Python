class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        passed_nums = []
        for i in range(len(nums)):
            if nums[i] in passed_nums:
                continue
            else:
                for j in range(len(nums)):
                    if nums[i] == nums[j] and i != j:
                        passed_nums.append(nums[i])
                        break
        for num in nums:
            if num not in passed_nums:
                return num

            
