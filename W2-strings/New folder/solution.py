class Solution:
    def combineWithOtherDigits(self, result, digits, previous, index, digitLetterMapping):
        if index == len(digits):
            result.append(previous)
            return
        letters = digitLetterMapping[int(digits[index])]
        for i in range(0, len(letters)):
            self.combineWithOtherDigits(
                result, digits, previous + letters[i], index + 1, digitLetterMapping)

    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) == 0:
            return []

        digitToLetters = [
            "0",
            "1",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"
        ]

        result = []

        self.combineWithOtherDigits(result, digits, "", 0, digitToLetters)
        return result
