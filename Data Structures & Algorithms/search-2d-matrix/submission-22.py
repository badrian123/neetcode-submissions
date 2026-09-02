class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        while l <= r:
            m = (l + r)//2
            
            if target < matrix[m][0]:
                r = m -1
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                break
        
        selected_row = (l + r)// 2
        l, r = 0, len(matrix[selected_row])-1
        while l <= r:
            
            m = (l + r)// 2
            if target < matrix[selected_row][m]:
                r = m -1
            elif target > matrix[selected_row][m]:
                l = m + 1
            else:
                return True
        return False                