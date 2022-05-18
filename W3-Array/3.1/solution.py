class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        ans = []

        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            low = i + 1
            hi = len(nums) - 1
            while low < hi:
                sum = nums[i] + nums[low] + nums[hi]
                if sum == 0:
                    ans.append((nums[i], nums[low], nums[hi]))
                    low += 1
                    hi -= 1
                    while nums[low] == nums[low - 1] and low < hi:
                        low += 1
                    while nums[hi] == nums[hi + 1] and low < hi:
                        hi -= 1
                elif sum < 0:
                    low += 1
                else:
                    hi -= 1

        return ans
