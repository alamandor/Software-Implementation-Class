class Solution:
    def rob(self, nums: List[int]) -> int:
        resultTable = [0 for _ in range(len(nums))]

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        resultTable[0] = nums[0]
        resultTable[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            resultTable[i] = max(resultTable[i - 2] +
                                 nums[i],  resultTable[i - 1])

        return max(resultTable[-1], resultTable[-2])
