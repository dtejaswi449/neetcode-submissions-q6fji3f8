class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        col = len(matrix[0]) - 1
        start = 0
        end = len(matrix) - 1
        while start <= end:
            mid = (start + end)//2
            if matrix[mid][0] <= target <= matrix[mid][col]:
                a = 0
                s = matrix[mid][a]
                e = matrix[mid][col]
                while a <= col:
                    m = (a + col)//2
                    if matrix[mid][m] > target:
                        col = m - 1
                    elif matrix[mid][m] < target:
                        a = m + 1
                    else:
                        return True
                return False
            elif matrix[mid][0] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False




        