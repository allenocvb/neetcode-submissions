class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix) # row
        n = len(matrix[0]) # columns
        total_len = m * n

        l = 0
        r = total_len - 1

        while l <= r:
            mid = (l+r) // 2

            i = mid // n
            j = mid % n

            number = matrix[i][j]

            if target == number:
                return True
            elif target > number:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
        