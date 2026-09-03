class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Select
        l, r = 0, len(matrix)-1
        while l <= r:
            m = (l + r)//2
            #Now how to determine. Well, with the middle front & back values.
            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                break
        #Disect        
        selected_row = (l+r)//2
        l, r = 0, len(matrix[selected_row])-1
        while l <= r:
            m = (l + r) // 2
            #I am in the row.
            #Now, what do I need to do?
            #I am going to try to find this target in the row.
            #Therefore, I am going to compare the middle and if it is

            if target > matrix[selected_row][m]:
                l = m + 1
            elif target < matrix[selected_row][m]:
                r = m -1
            else:
                return True
        return False