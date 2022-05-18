class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def kPairsPresent(mid):  # two pointers
            count, i, j = 0, 0, 0
            while i < n or j < n:
                while j < n and nums[j] - nums[i] <= mid:
                    j += 1
                count += j - i - 1
                i += 1
            return count >= k

        nums.sort()
        l, r = 0, nums[-1] - nums[0]
        while l < r:
            mid = l + (r - l) // 2
            if kPairsPresent(mid):
                r = mid
            else:
                l = mid + 1
        return l
