class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hTable = {}
        for i in range(len(s)):
            hTable[s[i]] = i
        res = []
        left = right = 0
        i = 0
        while i < len(s):
            right = max(right, hTable[s[i]])
            if i == right:
                res.append(right - left + 1)
                left = i + 1
            i += 1
        return res
