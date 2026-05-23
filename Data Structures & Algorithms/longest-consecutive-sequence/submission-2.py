class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        store = set()
        longest = 0

        for i in range(len(nums)):
            store.add(nums[i])

        for num in store:
            # start sequence
            if num - 1 not in store:
                length = 1
                while num + length in store:
                    length += 1
                longest = max(longest, length)

        return longest
