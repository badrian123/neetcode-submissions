class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #I need to select.
        #Then I need to disect

        #Going to use two pointer.
        #Going to use binary search.
        #Going to use the front and end of the row to determine which row to focus on.

        #Then use <= and >= for the added benefits of bineary search.

        #This gives me all of the rows i need
        l, r = 0, len(matrix)-1
        while l <= r:
            middle = (l + r)//2
            if target > matrix[middle][-1]:
                l = middle + 1
            elif target < matrix[middle][0]:
                r = middle - 1
            else:
                break
        
        selected_row = (l + r ) // 2
        l, r = 0, len(matrix[selected_row])-1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[selected_row][m]:
                l = m + 1
            elif target < matrix[selected_row][m]:
                r = m - 1
            else:
                return True
        return False


