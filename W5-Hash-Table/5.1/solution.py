class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        start = 0
        end = 0
        substringLength = 0
        unique = set()
        while end < len(s):
            if s[end] not in unique:
                unique.add(s[end])
                end += 1
                substringLength = max(substringLength, len(unique))
            else:
                unique.remove(s[start])
                start += 1
        return substringLength
