class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        p1 = nums[0]
        p2 = nums[0]
        while True:
            p1 = nums[p1]
            p2 = nums[nums[p2]]
            if p1 == p2:
                break
        p2 = nums[0]
        while p2 != p1:
            p2 = nums[p2]
            p1 = nums[p1]
        return p1
