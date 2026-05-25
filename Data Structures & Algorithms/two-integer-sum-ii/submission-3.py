class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)):
            target_now = target - numbers[i]
            for j in range(i + 1, len(numbers)):
                if target_now == numbers[j]:
                    return [i + 1, j + 1]

