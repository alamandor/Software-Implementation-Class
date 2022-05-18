class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_map = {}
        for n in nums:
            if n not in count_map:
                count_map[n] = 1
            else:
                count_map[n] += 1

        for i in count_map:
            if count_map[i] == 1:
                return i
