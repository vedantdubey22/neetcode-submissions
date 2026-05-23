class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans = []
        # n = len(nums)
        # for i in range((2 * n)):
        #     ans.append(nums[i % n])

        # return ans

        ans = []
        for i in nums:
            ans.append(i)
        for i in nums:
            ans.append(i)

        return ans