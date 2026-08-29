class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        while l <= r:
            middle = (l+r)//2
            if matrix[middle][0] > target:
                r -= 1
            elif matrix[middle][-1] < target:
                l += 1
            else:
                break

        selected_row = (l+r) // 2
        l, r = 0, len(matrix[selected_row])-1

        while l <= r:
            m = (l+r) // 2
            if matrix[selected_row][m] > target:
                r -= 1
            elif matrix[selected_row][m] < target:
                l += 1
            else:
                return True
        return False