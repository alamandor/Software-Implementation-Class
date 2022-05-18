class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''

        if strs is None or len(strs) == 0:
            return ''

        shortestStringLength = len(strs[0])

        for i in range(1, len(strs)):
            shortestStringLength = min(shortestStringLength, len(strs[i]))

        for i in range(0, shortestStringLength):
            letter = strs[0][i]

            for j in range(0, len(strs)):
                if strs[j][i] != letter:
                    return res
            res += letter
        return res
