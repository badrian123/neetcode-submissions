class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, len(matrix)-1
        while L <= R:
            middle_row = (L+R) // 2
            if target > matrix[middle_row][-1]:
                L = middle_row + 1
            elif target < matrix[middle_row][0]:
                R = middle_row - 1
            else:
                break
        if not (L <= R):
            return False

        selected_row = (L+R) // 2
        l, r = 0, len(matrix[selected_row])-1

        while l <= r:
            m = (l+r) // 2
            if matrix[selected_row][m] > target:
                r = m - 1
            elif matrix[selected_row][m] < target:
                l = m + 1
            else:
                return True
        return False