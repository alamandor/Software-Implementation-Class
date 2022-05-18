class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        x = len(matrix)
        y = len(matrix[0])

        l, r = 0, (x*y)-1
        while l <= r:
            mid = (l+r)//2
            row = mid//y
            col = mid % y
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
