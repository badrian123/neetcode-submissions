class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #I know that I got to find direction.
        #Then I need to disect the row

        #Now, I am going to use two point and binary search.
        #Then I am going to 

        #Selection
        l, r = 0, len(matrix)-1 #This should give me the three rows.
        while l <= r:
            #This is the middle row.
            m = (r + l)//2

            if target < matrix[m][0]:
                r = m - 1 
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                break

        #Disection        
        selected_row = (r + l)//2
        l, r = 0, len(matrix[selected_row])-1

        while l <= r:
            m = (r + l)//2
            if target < matrix[selected_row][m]:
                r = m - 1
            elif target > matrix[selected_row][m]:
                l = m + 1
            else:
                return True
        return False