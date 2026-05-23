class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ans = []
        seen = {}

        for i in range(len(nums)):
            target_num = target - nums[i]
            if target_num in seen:
                return [seen[target_num], i]
            else:
                seen[nums[i]] = i