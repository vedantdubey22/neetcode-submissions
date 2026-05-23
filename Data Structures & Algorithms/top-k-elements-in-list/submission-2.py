class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        countNums = {}
        ans = []

        for i in range(len(nums)):
            countNums[nums[i]] = countNums.get(nums[i], 0) + 1

        sortedNums = dict(sorted(countNums.items(), key=lambda x: x[1], reverse=True))

        for i in sortedNums:
            if len(ans) < k:
                ans.append(i)
                    

        return ans
           
